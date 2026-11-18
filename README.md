# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->
## Stretch Features Declared Before Building

Before implementing the service, I decided to attempt all three stretch features:

1. **Third signal:** I will add a third signal that measures source-attribution cues such as citations, quotations, URLs, and named references. It will be weighted separately from the semantic model and stylometry signals.

2. **Content lookup:** I will add `GET /content/<id>` so a caller can retrieve one item’s current decision and status.

3. **Verified-human path:** I will add a separate verification step through which a creator earns a human-verification credential. That credential will appear on the creator’s later submission responses.
## What This Does

Provenance Guard is a Flask backend service that gives a writing platform a cautious estimate of whether submitted text resembles AI-generated or human writing. It does not prove authorship. Because falsely accusing a real writer is more harmful than missing some AI-written text, uncertain results receive a neutral label and writers can appeal.

### Submission path

1. A caller sends `text` and an optional `creator_id` to `POST /submit`.
2. The route rejects missing, non-string, empty, whitespace-only, or over-5,000-character text before loading the detector.
3. `detector.py::model_signal` measures how predictable the writing is to GPT-2. Lower perplexity produces a higher AI-likelihood score.
4. `stylometry.py::style_signal` measures sentence-length variation, vocabulary variety, and punctuation density.
5. `provenance.py::source_signal` checks for visible source-attribution cues such as URLs, quotations, and attribution phrases.
6. `scoring.py::combine_signals` combines the three scores into one number from `0.0` (more human-like) to `1.0` (more AI-like).
7. `scoring.py::score_to_label` maps the combined score to high-confidence human, unsure, or high-confidence AI.
8. The service creates a `content_id`, records the decision and individual signal scores in `logs/audit.jsonl`, and returns the result.
9. A writer can appeal through `POST /appeal`. The service preserves the original decision, adds an appeal event, and changes the current status to `under_review`.

### False-positive path

If human writing receives an AI label, the response presents it as an automated estimate rather than proof. The writer can submit the returned `content_id` and an explanation to `/appeal`. The service records both events instead of overwriting the original decision, allowing a reviewer to see what happened and in what order.

### Endpoint contracts

#### `POST /submit`

Input:

- `text` — required string containing the writing to examine.
- `creator_id` — optional writer identifier; invalid or missing values become `anonymous`.

Output:

- `content_id`
- `guess`
- `confidence` — the combined AI-likelihood score
- `label`
- `model_score`
- `style_score`
- `source_score`
- `creator_credential`

#### `POST /appeal`

Input:

- `content_id`
- `reasoning`

Output:

- `content_id`
- `status`
- a plain-language confirmation message

---

## Signals and Scoring

### Signal one — the model signal

**What it measures:** `detector.py::model_signal` measures the text’s perplexity under GPT-2. Text that GPT-2 finds easier to predict receives a higher AI-likelihood score.

**Why that might differ between human and AI writing:** Generated prose often follows statistically common and predictable word sequences. Human writing can contain more personal, irregular, or surprising choices.

**What it can't see:** Predictability is not proof of authorship. Formal, plain, second-language, or highly edited human writing can be predictable, while AI writing containing unusual wording can appear less predictable.

### Signal two — the style signal

**What it measures:** `stylometry.py::style_signal` combines normalized sentence-length spread, type-token ratio, and punctuation density. Low structural variation produces a higher AI-likelihood score.

**Why that might differ between human and AI writing:** Generated prose often uses evenly sized sentences and repeated, conventional structures. Human writing may be more uneven, mixing fragments, questions, long explanations, and different punctuation.

**What it can't see:** This signal cannot understand meaning or authorship. A person who writes in a simple, consistent style may score as AI-like, while adding punctuation, sentence breaks, quotations, or typos can make AI-generated text appear more human-like.

### Signal three — source attribution

**What it measures:** `provenance.py::source_signal` looks for visible URLs, quotations, and phrases such as “according to” or “data from.” No visible source evidence receives a neutral score of `0.50`; source cues can lower the score toward `0.00`.
**Why it might differ:** Traceable sources give readers something outside the prose that they can inspect, so this signal can reduce suspicion when visible provenance is present.

**What it can't see:** It cannot verify that a citation is genuine, that a quotation is accurate, or that the source supports the claim. AI-generated text can fabricate citations, so this signal receives the smallest weight.

### The combining rule

**The rule:** All three signals point in the same direction: higher means more AI-like. The model and style signals receive equal primary weight. Source attribution receives a smaller weight because it is useful supporting evidence but can be fabricated. When the primary signals disagree, their average generally moves the result toward `unsure`, which reduces false accusations.

**The numbers:**

```text
combined score =
    (0.40 × model score)
  + (0.40 × style score)
  + (0.20 × source score)
```

**Where it lives:** `scoring.py::combine_signals`

**A case where my signals split, and what my rule does with it:** The repetitive test text produced a model score of `0.3373` but a style score of `0.6071`. The model signal leaned human while the style signal leaned AI. With a neutral source score of `0.50`, the weighted combination is approximately `0.4778`, placing the text in the `unsure` band instead of making a strong accusation.

---

## Label Variants

| Label | Score range | The exact text a reader sees |
|---|---:|---|
| high-confidence human | `0.00 ≤ score ≤ 0.35` | `This text shows strong signals of human writing.` |
| unsure | `0.35 < score < 0.65` | `The authorship of this text is uncertain. Review is recommended.` |
| high-confidence AI | `0.65 ≤ score ≤ 1.00` | `This text shows strong signals of AI-generated writing. This automated estimate may be appealed.` |

**Why I worded the “unsure” one this way:** It clearly states that the system cannot determine authorship and recommends review without implying that the writer did something wrong. This matters because the person receiving the label may have written every word themselves.

---

## Sample Run

### A submission

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text":"I drafted this paragraph after reviewing my class notes. Some parts were easy; others took three rewrites before they sounded right.","creator_id":"dyuthi"}'
```

```json
{
  "confidence": 0.4223,
  "content_id": "4ee42bde-2df6-4b2d-8793-8dd2972f3995",
  "creator_credential": "verified-human",
  "guess": "unsure",
  "label": "The authorship of this text is uncertain. Review is recommended.",
  "model_score": 0.3075,
  "source_score": 0.5,
  "style_score": 0.4983
}
```

### An appeal

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id":"4ee42bde-2df6-4b2d-8793-8dd2972f3995","reasoning":"I wrote this paragraph myself from my class notes and would like a human review."}'
```

```json
{
  "content_id": "4ee42bde-2df6-4b2d-8793-8dd2972f3995",
  "message": "Your appeal was recorded and the submission is under review.",
  "status": "under_review"
}
```

### What the log shows afterwards

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.4223,
      "content_id": "4ee42bde-2df6-4b2d-8793-8dd2972f3995",
      "creator_credential": "verified-human",
      "creator_id": "dyuthi",
      "guess": "unsure",
      "label": "The authorship of this text is uncertain. Review is recommended.",
      "model_score": 0.3075,
      "source_score": 0.5,
      "status": "decided",
      "style_score": 0.4983,
      "timestamp": "2026-10-29T02:07:52+00:00"
    },
    {
      "content_id": "4ee42bde-2df6-4b2d-8793-8dd2972f3995",
      "creator_id": "dyuthi",
      "event": "appeal",
      "reasoning": "I wrote this paragraph myself from my class notes and would like a human review.",
      "status": "under_review",
      "timestamp": "2026-10-29T02:10:20+00:00"
    }
  ]
}
```

### Stretch feature — third signal

A submission with source-attribution evidence produced:

```json
{
  "confidence": 0.3206,
  "content_id": "afbc4ce6-a0d3-4e3f-9346-ae59513a0c5d",
  "guess": "human",
  "label": "This text shows strong signals of human writing.",
  "model_score": 0.4169,
  "source_score": 0.0,
  "style_score": 0.3845
}
```

The third signal receives 20% of the combined score. It lowered the score because the text included an attribution phrase and a URL, but it did not replace the model or style signals.

### Stretch feature — `GET /content/<id>`

```bash
$ curl "http://127.0.0.1:5000/content/4ee42bde-2df6-4b2d-8793-8dd2972f3995"
```

```json
{
  "appeal_count": 1,
  "combined_score": 0.4223,
  "content_id": "4ee42bde-2df6-4b2d-8793-8dd2972f3995",
  "creator_credential": "verified-human",
  "creator_id": "dyuthi",
  "guess": "unsure",
  "label": "The authorship of this text is uncertain. Review is recommended.",
  "model_score": 0.3075,
  "source_score": 0.5,
  "status": "under_review",
  "style_score": 0.4983,
  "appeal_count": 1
}
```

The complete response also contains the ordered `history` list with the original decision and appeal.

### Stretch feature — verified-human path

```bash
$ curl -X POST http://127.0.0.1:5000/verify-human \
  -H "Content-Type: application/json" \
  -d '{"creator_id":"dyuthi","attestation":"I confirm that I am the human author."}'
```

```json
{
  "creator_id": "dyuthi",
  "credential": "verified-human",
  "message": "Verified-human credential awarded.",
  "verification_method": "authorship-attestation",
  "verified_at": "2026-10-29T02:06:05+00:00"
}
```

The credential is stored for the creator and appears on later submissions as `"creator_credential": "verified-human"`. This is a lightweight authorship attestation, not identity verification, so it does not automatically change the detector score or label.

---

## How I Used AI

### Moment 1

- **What I asked for:** I asked for help checking whether my five proposed acceptance criteria were numerical, reproducible, and connected to the risks of this service.
- **What came back:** AI identified measurable structures for false positives, score separation, label reachability, appeals, and malformed input.
- **What I changed:** I selected the targets, kept the higher standard for deterministic appeal and validation behavior, and corrected the bad-input criterion so it did not incorrectly require `creator_id`.

### Moment 2

- **What I asked for:** I asked for help debugging the submission route while connecting the model, style, source-attribution, and verified-human features.
- **What came back:** AI helped identify missing imports, a removed `guess, label` assignment, and an indentation error that left `creator_credential` undefined.
- **What I changed:** I added the missing imports and assignment, moved the credential lookup outside the conditional block, reran syntax checks, and verified every fix using real `curl` responses and audit-log entries.
<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---
## Unit 8 Stretch Features Declared Before Testing

Before running the Unit 8 attack set or changing the detector, I decided to attempt these stretch features:

1. **Per-creator limits:** `/submit` requests will be limited using `creator_id` rather than only the network address. This should catch one creator sending many variations even if requests come through different addresses. The tradeoff is that a malicious caller can rotate fake creator IDs, while multiple legitimate users sharing an address will no longer affect one another.

2. **Second measured improvement:** After diagnosing the untouched before-run and measuring one improvement, I will make one additional diagnosis-driven change. I will run the complete attack set and all five criteria again in the same format and report whether it helped and what it cost elsewhere.

3. **Three attacks against another system:** If another team makes its service available, I will write three original attacks, record the system tested, and report the response and outcome of each attack. I will report unsuccessful attacks honestly.


## Rate Limiting

**My limits:** 8 submissions per minute and 100 submissions per day.

**Why those numbers:** Eight submissions per minute permits several genuine revisions while stopping rapid threshold probing. One hundred per day is well above normal individual use but blocks sustained automated testing.

**What counts as one caller:** Requests are keyed primarily by `creator_id`, with the network address as a fallback. This avoids penalizing unrelated writers sharing an address, but a malicious caller could rotate fake creator IDs.

**Flood result produced by `run_attacks.py --flood 15`:**

```text
200 200 200 200 200 200 200 200 429 429 429 429 429 429 429
```

The limiter accepted eight rapid submissions and rejected seven. Rejections were recorded in `logs/audit.jsonl` with `status: "rejected"` and `reason: "rate_limited"`.

---

## Attack Run — Before

The untouched service was tested against all 56 staff attacks by `run_attacks.py::main`. Full evidence is in `results/attack_run_2026-11-04_1946_before.md`.

**Summary:** 38 HELD and 18 BROKE.

| ID | Family | HTTP status | Guess | Verdict |
|---|---|---:|---|---|
| EV01 | `evasion` | 200 | unsure | **BROKE** |
| EV02 | `evasion` | 200 | unsure | **BROKE** |
| EV03 | `evasion` | 200 | unsure | **BROKE** |
| EV04 | `evasion` | 200 | unsure | **BROKE** |
| EV05 | `evasion` | 200 | human | **BROKE** |
| EV06 | `evasion` | 200 | unsure | **BROKE** |
| EV07 | `evasion` | 200 | unsure | **BROKE** |
| EV08 | `evasion` | 200 | unsure | **BROKE** |
| EV09 | `evasion` | 200 | unsure | **BROKE** |
| EV10 | `evasion` | 200 | ai | **HELD** |
| FP01 | `false_positive` | 200 | unsure | **HELD** |
| FP02 | `false_positive` | 200 | unsure | **HELD** |
| FP03 | `false_positive` | 200 | unsure | **HELD** |
| FP04 | `false_positive` | 200 | unsure | **HELD** |
| FP05 | `false_positive` | 200 | ai | **BROKE** |
| FP06 | `false_positive` | 200 | unsure | **HELD** |
| FP07 | `false_positive` | 200 | unsure | **HELD** |
| FP08 | `false_positive` | 200 | human | **HELD** |
| PI01 | `prompt_injection` | 200 | unsure | **HELD** |
| PI02 | `prompt_injection` | 200 | human | **HELD** |
| PI03 | `prompt_injection` | 200 | unsure | **HELD** |
| PI04 | `prompt_injection` | 200 | unsure | **HELD** |
| PI05 | `prompt_injection` | 200 | unsure | **HELD** |
| PI06 | `prompt_injection` | 200 | unsure | **HELD** |
| MF01 | `malformed` | 400 | — | **HELD** |
| MF02 | `malformed` | 500 | — | **BROKE** |
| MF03 | `malformed` | 200 | unsure | **BROKE** |
| MF04 | `malformed` | 200 | unsure | **BROKE** |
| MF05 | `malformed` | 200 | ai | **BROKE** |
| MF06 | `malformed` | 200 | ai | **BROKE** |
| MF07 | `malformed` | 200 | ai | **BROKE** |
| MF08 | `malformed` | 400 | — | **HELD** |
| RQ01 | `malformed_request` | 400 | — | **HELD** |
| RQ02 | `malformed_request` | 200 | unsure | **BROKE** |
| RQ03 | `malformed_request` | 400 | — | **HELD** |
| RQ04 | `malformed_request` | 400 | — | **HELD** |
| RQ05 | `malformed_request` | 400 | — | **HELD** |
| RQ06 | `malformed_request` | 200 | human | **BROKE** |
| RQ07 | `malformed_request` | 400 | — | **HELD** |
| RQ08 | `malformed_request` | 400 | — | **HELD** |
| RQ09 | `malformed_request` | 400 | — | **HELD** |
| RQ10 | `malformed_request` | 400 | — | **HELD** |
| RQ11 | `malformed_request` | 400 | — | **HELD** |
| RQ12 | `malformed_request` | 400 | — | **HELD** |
| FL01_01 | `flood_same_creator` | 200 | unsure | **HELD** |
| FL01_02 | `flood_same_creator` | 200 | unsure | **HELD** |
| FL01_03 | `flood_same_creator` | 200 | unsure | **HELD** |
| FL01_04 | `flood_same_creator` | 200 | unsure | **HELD** |
| FL01_05 | `flood_same_creator` | 200 | unsure | **HELD** |
| FL01_06 | `flood_same_creator` | 200 | unsure | **HELD** |
| FL01_07 | `flood_same_creator` | 200 | unsure | **HELD** |
| FL01_08 | `flood_same_creator` | 200 | unsure | **HELD** |
| FL01_09 | `flood_same_creator` | 429 | — | **HELD** |
| FL01_10 | `flood_same_creator` | 429 | — | **HELD** |
| FL01_11 | `flood_same_creator` | 429 | — | **HELD** |
| FL01_12 | `flood_same_creator` | 429 | — | **HELD** |

### Ten audit entries

```json
[
  {
    "combined_score": 0.3898,
    "content_id": "77a70228-eaeb-4548-830e-34fe8a893a05",
    "creator_credential": null,
    "creator_id": "attacker_EV01",
    "guess": "unsure",
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "model_score": 0.1635,
    "source_score": 0.5,
    "status": "decided",
    "style_score": 0.5609,
    "timestamp": "2026-11-05T01:46:24+00:00"
  },
  {
    "combined_score": 0.3203,
    "content_id": "c0d11e1c-75e8-4d67-a754-01d60e5c7dc5",
    "creator_credential": null,
    "creator_id": "attacker_EV05",
    "guess": "human",
    "label": "This text shows strong signals of human writing.",
    "model_score": 0.3212,
    "source_score": 0.5,
    "status": "decided",
    "style_score": 0.2296,
    "timestamp": "2026-11-05T01:46:24+00:00"
  },
  {
    "combined_score": 0.7801,
    "content_id": "4aec8b0d-0b60-43de-99c9-d6406472191b",
    "creator_credential": null,
    "creator_id": "attacker_EV10",
    "guess": "ai",
    "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
    "model_score": 0.9792,
    "source_score": 0.5,
    "status": "decided",
    "style_score": 0.7211,
    "timestamp": "2026-11-05T01:46:25+00:00"
  },
  {
    "combined_score": 0.6671,
    "content_id": "d25fb058-54fb-4812-8e86-f2c427bf97fc",
    "creator_credential": null,
    "creator_id": "attacker_FP05",
    "guess": "ai",
    "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
    "model_score": 0.8005,
    "source_score": 0.5,
    "status": "decided",
    "style_score": 0.6173,
    "timestamp": "2026-11-05T01:46:25+00:00"
  },
  {
    "combined_score": 0.4605,
    "content_id": "1476f9e6-2457-4d03-b4d1-6ad0f3dfa536",
    "creator_credential": null,
    "creator_id": "attacker_PI04",
    "guess": "unsure",
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "model_score": 0.4998,
    "source_score": 0.5,
    "status": "decided",
    "style_score": 0.4014,
    "timestamp": "2026-11-05T01:46:25+00:00"
  },
  {
    "combined_score": 0.8514,
    "content_id": "c0ad4806-3ca0-4f5d-bbf8-f61fed73ca47",
    "creator_credential": null,
    "creator_id": "attacker_MF07",
    "guess": "ai",
    "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
    "model_score": 0.9064,
    "source_score": 0.5,
    "status": "decided",
    "style_score": 0.972,
    "timestamp": "2026-11-05T01:46:25+00:00"
  },
  {
    "combined_score": null,
    "content_id": null,
    "creator_id": "flood_tester",
    "event": "rejected",
    "guess": null,
    "label": null,
    "limit": "8 per 1 minute",
    "model_score": null,
    "reason": "rate_limited",
    "status": "rejected",
    "style_score": null,
    "timestamp": "2026-11-05T01:36:15+00:00"
  },
  {
    "combined_score": null,
    "content_id": null,
    "creator_id": "flood_tester",
    "event": "rejected",
    "guess": null,
    "label": null,
    "limit": "8 per 1 minute",
    "model_score": null,
    "reason": "rate_limited",
    "status": "rejected",
    "style_score": null,
    "timestamp": "2026-11-05T01:36:15+00:00"
  },
  {
    "combined_score": null,
    "content_id": null,
    "creator_id": "flood_tester",
    "event": "rejected",
    "guess": null,
    "label": null,
    "limit": "8 per 1 minute",
    "model_score": null,
    "reason": "rate_limited",
    "status": "rejected",
    "style_score": null,
    "timestamp": "2026-11-05T01:36:15+00:00"
  },
  {
    "combined_score": null,
    "content_id": null,
    "creator_id": "flood_tester",
    "event": "rejected",
    "guess": null,
    "label": null,
    "limit": "8 per 1 minute",
    "model_score": null,
    "reason": "rate_limited",
    "status": "rejected",
    "style_score": null,
    "timestamp": "2026-11-05T01:36:15+00:00"
  }
]
```

**Worst outcome:** `FP05` was genuine human technical documentation but received a high-confidence AI label at `0.6671`. Both the model score (`0.8005`) and style score (`0.6173`) were high, pushing it above the `0.65` threshold. This is the costliest failure because it directly accuses a real writer.

---

## Run Log and Verdicts — Before

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Human writing avoids high-confidence AI labels | At most 1 of 10 labelled AI in every run | 0/10 — PASS | 0/10 — PASS | 0/10 — PASS | **MET** |
| 2. Clearly AI and clearly human writing have separated scores | AI average at least 0.20 above human average | +0.0925 — FAIL | +0.0925 — FAIL | +0.0925 — FAIL | **MISSED** |
| 3. All three labels are reachable | Human, unsure, and AI all appear | 2/3 — FAIL | 2/3 — FAIL | 2/3 — FAIL | **MISSED** |
| 4. Every valid appeal changes status and is logged | 5 of 5 | 5/5 — PASS | 5/5 — PASS | 5/5 — PASS | **MET** |
| 5. Invalid submissions are rejected safely | 5 of 5 return 400 without crashing | 5/5 — PASS | 5/5 — PASS | 5/5 — PASS | **MET** |

### Real output from one trial

Produced by `run_eval.py::main` through `app.py::submit`; the complete run is in `results/run_2026-11-04_2000_before.md`.

```json
[
  {
    "status": 200,
    "content_id": "fd72a3f5-6d54-46ca-9ff2-9e4f6dd4c2b5",
    "guess": "unsure",
    "confidence": 0.5205,
    "model_score": 0.6988,
    "style_score": 0.3524,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Obesity, body weight, and physical activity were chosen as the main re"
  },
  {
    "status": 200,
    "content_id": "b6395a73-b3de-40a3-a875-cff2ec026623",
    "guess": "unsure",
    "confidence": 0.542,
    "model_score": 0.6228,
    "style_score": 0.4823,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The WCRF/AICR scoring system evaluates how closely a person follows ca"
  },
  {
    "status": 200,
    "content_id": "b5ce73b3-c349-4e9c-9a48-6a660db513fc",
    "guess": "unsure",
    "confidence": 0.4504,
    "model_score": 0.4502,
    "style_score": 0.4259,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Current food-tracking technologies may be unable to distinguish foods "
  },
  {
    "status": 200,
    "content_id": "2470a630-322c-4239-9fc8-706eaf55eeb2",
    "guess": "unsure",
    "confidence": 0.5025,
    "model_score": 0.3641,
    "style_score": 0.6422,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The device includes a Time of Flight depth sensor and an Inertial Meas"
  },
  {
    "status": 200,
    "content_id": "481cdf65-627e-4c2d-9401-3edf43ddebaa",
    "guess": "unsure",
    "confidence": 0.4437,
    "model_score": 0.3294,
    "style_score": 0.5298,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The proposed system estimates energy expenditure using wearable physic"
  },
  {
    "status": 200,
    "content_id": "09931fdb-b8e6-467e-973e-c5f939c2a845",
    "guess": "human",
    "confidence": 0.3162,
    "model_score": 0.1891,
    "style_score": 0.3515,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "The presentation emphasizes the feasibility of privacy-preserving food"
  },
  {
    "status": 200,
    "content_id": "663dfb7a-40d2-4531-9818-77f9b5ce22ff",
    "guess": "unsure",
    "confidence": 0.546,
    "model_score": 0.5548,
    "style_score": 0.5603,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The main objective of Aim 1 is to develop and validate the wearable AI"
  },
  {
    "status": 200,
    "content_id": "74a5865c-dad7-4462-bd38-c7c9bbd811b6",
    "guess": "unsure",
    "confidence": 0.4322,
    "model_score": 0.3443,
    "style_score": 0.4861,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Aim 2 proposes a twelve-week real-world pilot involving thirty partici"
  },
  {
    "status": 200,
    "content_id": "f877aaab-9ff5-4931-baa4-57e552575c45",
    "guess": "unsure",
    "confidence": 0.4054,
    "model_score": 0.3968,
    "style_score": 0.3668,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Our team believes depth sensing is a useful and privacy-preserving app"
  },
  {
    "status": 200,
    "content_id": "4cc4c204-33a3-402e-9a0a-5d556c3f46a5",
    "guess": "unsure",
    "confidence": 0.4702,
    "model_score": 0.4937,
    "style_score": 0.4318,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Our team recommends funding the project as a pilot study with some res"
  }
]
```

### Diagnoses

**Criterion 2 — combining rule:** The model signal separated the two groups by `+0.2524`, but the style signal moved in the wrong direction by `−0.0211` and the source signal was neutral. Weights of `0.40/0.40/0.20` diluted the final difference to `+0.0925`, below the `+0.20` target.

**Criterion 3 — combining rule and label mapping:** None of the three fixed calibration inputs crossed the `0.65` AI threshold. Neutral source evidence and mixed model/style scores kept them human or unsure. The criterion was therefore missed, even though other attack inputs showed the AI label itself was reachable.

**Evasions `EV01–EV09`:** Typos raised vocabulary variety, uneven sentence lengths looked human, quotations and human openings changed style statistics, unusual vocabulary raised perplexity, and short or heavily edited text weakened the model signal. The combined values stayed below the AI threshold. `EV10` held because both signals remained strongly AI-like.

**False positive `FP05`:** Predictable formal technical prose produced high model and style scores, so the label mapping accused a genuine writer.

**Malformed `MF02–MF06`:** The route checked type, emptiness, and total length but not whether usable prose existed. A single character reached the model and crashed; control characters, punctuation, a single enormous token, and emoji received unreliable decisions.

**Malformed `MF07`:** Arabic text was treated as AI because the English GPT-2 detector and current stylometry were not calibrated for that language.

**Requests `RQ02` and `RQ06`:** Missing or non-string creator identities were silently replaced with `anonymous` rather than rejected.

**Prompt injection:** All six held because submitted content was handled as data, not executed as instructions.

**Flood:** The first eight requests were accepted and the remaining requests were rejected with `429`.

---

## First Measured Improvement — Signal Reweighting

**What changed:** Model/style/source weights changed from `0.40/0.40/0.20` to `0.85/0.10/0.05`.

**Diagnosis behind it:** The model signal already supplied useful `+0.2524` separation, while style moved slightly backward and source attribution was neutral.

### Criteria Run — After First Improvement

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Human writing avoids high-confidence AI labels | At most 1 of 10 labelled AI | 1/10 — PASS | 1/10 — PASS | 1/10 — PASS | **MET** |
| 2. AI/human score separation | At least +0.20 | +0.2125 — PASS | +0.2125 — PASS | +0.2125 — PASS | **MET** |
| 3. All labels reachable | 3/3 labels | 1/3 — FAIL | 1/3 — FAIL | 1/3 — FAIL | **MISSED** |
| 4. Appeal path | 5/5 | 5/5 — PASS | 5/5 — PASS | 5/5 — PASS | **MET** |
| 5. Invalid input | 5/5 | 5/5 — PASS | 5/5 — PASS | 5/5 — PASS | **MET** |

### Attack Run — After First Improvement

Full evidence is in `results/attack_run_2026-11-04_2005_after_first.md`.

**Summary:** 34 HELD and 22 BROKE.

| ID | Family | HTTP status | Guess | Verdict |
|---|---|---:|---|---|
| EV01 | `evasion` | 200 | human | **BROKE** |
| EV02 | `evasion` | 200 | unsure | **BROKE** |
| EV03 | `evasion` | 200 | unsure | **BROKE** |
| EV04 | `evasion` | 200 | unsure | **BROKE** |
| EV05 | `evasion` | 200 | human | **BROKE** |
| EV06 | `evasion` | 200 | unsure | **BROKE** |
| EV07 | `evasion` | 200 | unsure | **BROKE** |
| EV08 | `evasion` | 200 | human | **BROKE** |
| EV09 | `evasion` | 200 | ai | **HELD** |
| EV10 | `evasion` | 200 | ai | **HELD** |
| FP01 | `false_positive` | 200 | unsure | **HELD** |
| FP02 | `false_positive` | 200 | ai | **BROKE** |
| FP03 | `false_positive` | 200 | ai | **BROKE** |
| FP04 | `false_positive` | 200 | ai | **BROKE** |
| FP05 | `false_positive` | 200 | ai | **BROKE** |
| FP06 | `false_positive` | 200 | ai | **BROKE** |
| FP07 | `false_positive` | 200 | ai | **BROKE** |
| FP08 | `false_positive` | 200 | human | **HELD** |
| PI01 | `prompt_injection` | 200 | unsure | **HELD** |
| PI02 | `prompt_injection` | 200 | human | **HELD** |
| PI03 | `prompt_injection` | 200 | unsure | **HELD** |
| PI04 | `prompt_injection` | 200 | unsure | **HELD** |
| PI05 | `prompt_injection` | 200 | unsure | **HELD** |
| PI06 | `prompt_injection` | 200 | unsure | **HELD** |
| MF01 | `malformed` | 400 | — | **HELD** |
| MF02 | `malformed` | 500 | — | **BROKE** |
| MF03 | `malformed` | 200 | human | **BROKE** |
| MF04 | `malformed` | 200 | human | **BROKE** |
| MF05 | `malformed` | 200 | ai | **BROKE** |
| MF06 | `malformed` | 200 | ai | **BROKE** |
| MF07 | `malformed` | 200 | ai | **BROKE** |
| MF08 | `malformed` | 400 | — | **HELD** |
| RQ01 | `malformed_request` | 400 | — | **HELD** |
| RQ02 | `malformed_request` | 200 | human | **BROKE** |
| RQ03 | `malformed_request` | 400 | — | **HELD** |
| RQ04 | `malformed_request` | 400 | — | **HELD** |
| RQ05 | `malformed_request` | 400 | — | **HELD** |
| RQ06 | `malformed_request` | 200 | human | **BROKE** |
| RQ07 | `malformed_request` | 400 | — | **HELD** |
| RQ08 | `malformed_request` | 400 | — | **HELD** |
| RQ09 | `malformed_request` | 400 | — | **HELD** |
| RQ10 | `malformed_request` | 400 | — | **HELD** |
| RQ11 | `malformed_request` | 400 | — | **HELD** |
| RQ12 | `malformed_request` | 400 | — | **HELD** |
| FL01_01 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_02 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_03 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_04 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_05 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_06 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_07 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_08 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_09 | `flood_same_creator` | 429 | — | **HELD** |
| FL01_10 | `flood_same_creator` | 429 | — | **HELD** |
| FL01_11 | `flood_same_creator` | 429 | — | **HELD** |
| FL01_12 | `flood_same_creator` | 429 | — | **HELD** |

**Did it help?** It raised measured separation from `+0.0925` to `+0.2125` and met Criterion 2. However, human false-positive attacks labeled AI rose from one to six, total broken attacks rose from 18 to 22, and the calibration inputs produced only the human label. The intended metric improved, but the safety tradeoff worsened.

---

## Second Measured Improvement — Request Validation

**What changed:** `/submit` now requires a non-empty string `creator_id` and at least three Unicode word-like tokens before either detector runs.

**Diagnosis behind it:** `MF02` crashed on one character; `MF03–MF06` contained no meaningful prose; and `RQ02`/`RQ06` showed that malformed identities were silently accepted.

### Criteria Run — After Second Improvement

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Human writing avoids high-confidence AI labels | At most 1 of 10 labelled AI | 1/10 — PASS | 1/10 — PASS | 1/10 — PASS | **MET** |
| 2. AI/human score separation | At least +0.20 | +0.2125 — PASS | +0.2125 — PASS | +0.2125 — PASS | **MET** |
| 3. All labels reachable | 3/3 labels | 1/3 — FAIL | 1/3 — FAIL | 1/3 — FAIL | **MISSED** |
| 4. Appeal path | 5/5 | 5/5 — PASS | 5/5 — PASS | 5/5 — PASS | **MET** |
| 5. Invalid input | 5/5 | 5/5 — PASS | 5/5 — PASS | 5/5 — PASS | **MET** |

### Attack Run — After Second Improvement

Full evidence is in `results/attack_run_2026-11-04_2019_after_second_final.md`.

**Summary:** 41 HELD and 15 BROKE.

| ID | Family | HTTP status | Guess | Verdict |
|---|---|---:|---|---|
| EV01 | `evasion` | 200 | human | **BROKE** |
| EV02 | `evasion` | 200 | unsure | **BROKE** |
| EV03 | `evasion` | 200 | unsure | **BROKE** |
| EV04 | `evasion` | 200 | unsure | **BROKE** |
| EV05 | `evasion` | 200 | human | **BROKE** |
| EV06 | `evasion` | 200 | unsure | **BROKE** |
| EV07 | `evasion` | 200 | unsure | **BROKE** |
| EV08 | `evasion` | 200 | human | **BROKE** |
| EV09 | `evasion` | 200 | ai | **HELD** |
| EV10 | `evasion` | 200 | ai | **HELD** |
| FP01 | `false_positive` | 200 | unsure | **HELD** |
| FP02 | `false_positive` | 200 | ai | **BROKE** |
| FP03 | `false_positive` | 200 | ai | **BROKE** |
| FP04 | `false_positive` | 200 | ai | **BROKE** |
| FP05 | `false_positive` | 200 | ai | **BROKE** |
| FP06 | `false_positive` | 200 | ai | **BROKE** |
| FP07 | `false_positive` | 200 | ai | **BROKE** |
| FP08 | `false_positive` | 200 | human | **HELD** |
| PI01 | `prompt_injection` | 200 | unsure | **HELD** |
| PI02 | `prompt_injection` | 200 | human | **HELD** |
| PI03 | `prompt_injection` | 200 | unsure | **HELD** |
| PI04 | `prompt_injection` | 200 | unsure | **HELD** |
| PI05 | `prompt_injection` | 200 | unsure | **HELD** |
| PI06 | `prompt_injection` | 200 | unsure | **HELD** |
| MF01 | `malformed` | 400 | — | **HELD** |
| MF02 | `malformed` | 400 | — | **HELD** |
| MF03 | `malformed` | 400 | — | **HELD** |
| MF04 | `malformed` | 400 | — | **HELD** |
| MF05 | `malformed` | 400 | — | **HELD** |
| MF06 | `malformed` | 400 | — | **HELD** |
| MF07 | `malformed` | 200 | ai | **BROKE** |
| MF08 | `malformed` | 400 | — | **HELD** |
| RQ01 | `malformed_request` | 400 | — | **HELD** |
| RQ02 | `malformed_request` | 400 | — | **HELD** |
| RQ03 | `malformed_request` | 400 | — | **HELD** |
| RQ04 | `malformed_request` | 400 | — | **HELD** |
| RQ05 | `malformed_request` | 400 | — | **HELD** |
| RQ06 | `malformed_request` | 400 | — | **HELD** |
| RQ07 | `malformed_request` | 400 | — | **HELD** |
| RQ08 | `malformed_request` | 400 | — | **HELD** |
| RQ09 | `malformed_request` | 400 | — | **HELD** |
| RQ10 | `malformed_request` | 400 | — | **HELD** |
| RQ11 | `malformed_request` | 429 | — | **HELD** |
| RQ12 | `malformed_request` | 400 | — | **HELD** |
| FL01_01 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_02 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_03 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_04 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_05 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_06 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_07 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_08 | `flood_same_creator` | 200 | human | **HELD** |
| FL01_09 | `flood_same_creator` | 429 | — | **HELD** |
| FL01_10 | `flood_same_creator` | 429 | — | **HELD** |
| FL01_11 | `flood_same_creator` | 429 | — | **HELD** |
| FL01_12 | `flood_same_creator` | 429 | — | **HELD** |

**Did it help?** Yes. The final attack run had no `500` responses. `MF02–MF06`, `RQ02`, and `RQ06` became safe `400` responses. Held attacks increased from 34 to 41 and broken attacks fell from 22 to 15. The cost is that legitimate submissions with fewer than three word-like tokens are rejected.

---

## What's Still Broken

Criterion 3 remains missed because the three fixed calibration inputs produce only the human label after reweighting. With more time, I would build a larger held-out calibration set of verified human, AI-generated, and genuinely uncertain writing, then tune thresholds and weights against that set.

Eight evasions still avoid the AI label by using typos, quotations, uneven sentence structure, unusual vocabulary, short context, or human editing. I would add adversarial calibration examples and length-aware scoring rather than patching individual strings.

Six genuine human false-positive attacks are still labeled AI. The `0.85` model weight improves average separation but harms predictable formal human writing. Before production, I would reduce that weight or raise the AI threshold and measure the effect on a larger human set.

`MF07` remains broken because Arabic is outside the reliable range of the English detector and stylometry. I would detect unsupported languages and return an uncertainty/unsupported-language response instead of an AI accusation.

**First fix with more time:** Human false positives. A missed AI detection lets generated text through; a false accusation directly harms a writer and forces that person to appeal.

**Production tradeoff:** I would widen the unsure band or reduce the model weight to lower false accusations. More AI text would pass as unsure, but that is safer than making genuine writers bear the cost of an unreliable detector.

### Stretch Feature Outcomes

**Per-creator limits:** Completed. This catches one creator sending rapid variations and prevents people sharing an address from consuming one another's quota. An attacker can still rotate fake IDs.

**Second measured improvement:** Completed. Baseline, first-improvement, and second-improvement runs use the full attack set and all five criteria.

**Three attacks against another system:** Not completed because another team's reachable service and results were unavailable; this point is not claimed.


📖 **How to run this project: [RUNNING.md](RUNNING.md)**

<!-- UNIT9_CAPSTONE_START -->

---

# Unit 9 Capstone — Batch Provenance Analysis

## What This Extends

This capstone extends **Provenance Guard**, the backend authorship-analysis
service built in Units 7 and 8. The original service evaluated one submission
at a time. The extension adds `POST /batch-submit`, which accepts between one
and ten submissions, preserves their order, isolates invalid items, returns
per-item results, and records both individual decisions and a batch summary.

A batch item follows the same three-signal pipeline as a normal submission:
`detector.py::model_signal`, `stylometry.py::style_signal`, and
`provenance.py::source_signal` feed `scoring.py::combine_signals`, which maps
the combined score to a reader-facing label. Each result has its own
`content_id`, signal scores, confidence, label, and timing.

## The Shape

I chose **Shape B: a local observable run with committed logs**. The service
runs locally as a Flask backend, while `run_batch_eval.py` sends real HTTP
requests and writes reproducible Markdown and JSON run records.

**Out of scope:** A browser frontend, public cloud deployment, authentication,
a persistent database, distributed workers, and a production job queue were
ruled out of scope. The local PyTorch and GPT-2 runtime also exceeds the memory
available on the free hosting option considered for this project.

## Running It

The documented local run path is in `RUNNING.md`. It requires Python 3.11 or
newer, the packages in `requirements.txt`, and the approximately 550 MB GPT-2
model downloaded by `python detector.py`. It does not require an API key.

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python detector.py
python test.py
python app.py
```

The service then answers at `http://127.0.0.1:5000`. In a second terminal, the
complete three-trial evaluation runs with:

```bash
source .venv/bin/activate
python run_batch_eval.py --label before
python run_batch_eval.py --label after_cache
```

The committed observable run records are:

- `results/batch_eval_2026-11-17_132311_before.json`
- `results/batch_eval_2026-11-17_132311_before.md`
- `results/batch_eval_2026-11-17_133109_after_cache.json`
- `results/batch_eval_2026-11-17_133109_after_cache.md`

## Instrumentation

`app.py::batch_submit` measures total request duration, average time per item,
and time spent in validation, model inference, stylometry, source analysis,
and score combination. Successful items receive `batch_id`, `batch_index`,
and `item_duration_ms` in `logs/audit.jsonl`. `audit.py::log_batch` records one
summary with input count, success and error counts, output guesses, duration,
stage totals, and status. Rejected batches are logged too.

`GET /health` exposes model-cache hits, misses, maximum size, and current size.
After the measured improvement it reported 54 hits, 6 misses, 6 cached texts,
and a maximum size of 256. A later verification run reported 114 hits and 8
misses, confirming continued cache reuse.

### Ten structured log entries

These entries were produced by `audit.py::log_batch` and retrieved through
`app.py::get_log`. Each records a timestamp, what came in (`input_count`), what
came out (`output_guesses`, success/error counts, or rejection), and duration.
The final entry proves that the failure path was recorded.

```json
[
  {
    "average_item_ms": 0.07,
    "batch_id": "1aea48f2-7472-488a-bf9c-3f87d1a0a347",
    "duration_ms": 0.371,
    "error_count": 1,
    "event": "batch_submission",
    "input_count": 5,
    "output_guesses": [
      "human",
      "human",
      "ai",
      "human"
    ],
    "processing_ms": 0.35,
    "stage_totals_ms": {
      "combining": 0.003,
      "model": 0.001,
      "source": 0.017,
      "style": 0.04,
      "validation": 0.015
    },
    "status": "partial",
    "success_count": 4,
    "timestamp": "2026-11-18T05:29:33+00:00"
  },
  {
    "average_item_ms": 0.086,
    "batch_id": "d112f8bb-ad9c-41c4-a7fb-2e449581bb8d",
    "duration_ms": 0.453,
    "error_count": 1,
    "event": "batch_submission",
    "input_count": 5,
    "output_guesses": [
      "human",
      "human",
      "ai",
      "human"
    ],
    "processing_ms": 0.429,
    "stage_totals_ms": {
      "combining": 0.003,
      "model": 0.001,
      "source": 0.017,
      "style": 0.041,
      "validation": 0.015
    },
    "status": "partial",
    "success_count": 4,
    "timestamp": "2026-11-18T05:29:33+00:00"
  },
  {
    "average_item_ms": 0.074,
    "batch_id": "cd480b99-ae5d-45c2-85d9-d34e711d6883",
    "duration_ms": 0.397,
    "error_count": 1,
    "event": "batch_submission",
    "input_count": 5,
    "output_guesses": [
      "human",
      "human",
      "ai",
      "human"
    ],
    "processing_ms": 0.369,
    "stage_totals_ms": {
      "combining": 0.003,
      "model": 0.001,
      "source": 0.017,
      "style": 0.038,
      "validation": 0.014
    },
    "status": "partial",
    "success_count": 4,
    "timestamp": "2026-11-18T05:29:33+00:00"
  },
  {
    "average_item_ms": 0.103,
    "batch_id": "2679108b-28ba-45d9-bec0-7a6e2a2608e1",
    "duration_ms": 0.551,
    "error_count": 0,
    "event": "batch_submission",
    "input_count": 5,
    "output_guesses": [
      "human",
      "human",
      "ai",
      "human",
      "human"
    ],
    "processing_ms": 0.514,
    "stage_totals_ms": {
      "combining": 0.004,
      "model": 0.002,
      "source": 0.023,
      "style": 0.055,
      "validation": 0.019
    },
    "status": "completed",
    "success_count": 5,
    "timestamp": "2026-11-18T05:29:33+00:00"
  },
  {
    "average_item_ms": 0.11,
    "batch_id": "eef55489-1d82-4f1b-ac42-0dab74413175",
    "duration_ms": 0.584,
    "error_count": 0,
    "event": "batch_submission",
    "input_count": 5,
    "output_guesses": [
      "human",
      "human",
      "ai",
      "human",
      "human"
    ],
    "processing_ms": 0.55,
    "stage_totals_ms": {
      "combining": 0.004,
      "model": 0.002,
      "source": 0.023,
      "style": 0.065,
      "validation": 0.02
    },
    "status": "completed",
    "success_count": 5,
    "timestamp": "2026-11-18T05:29:33+00:00"
  },
  {
    "average_item_ms": 0.089,
    "batch_id": "9b4db52c-77fc-4ad6-91c6-d5d760e476aa",
    "duration_ms": 0.475,
    "error_count": 0,
    "event": "batch_submission",
    "input_count": 5,
    "output_guesses": [
      "human",
      "human",
      "ai",
      "human",
      "human"
    ],
    "processing_ms": 0.447,
    "stage_totals_ms": {
      "combining": 0.004,
      "model": 0.002,
      "source": 0.022,
      "style": 0.049,
      "validation": 0.017
    },
    "status": "completed",
    "success_count": 5,
    "timestamp": "2026-11-18T05:29:33+00:00"
  },
  {
    "average_item_ms": 0.082,
    "batch_id": "c05b4cea-0a50-411c-8e72-9220a7765d01",
    "duration_ms": 0.43,
    "error_count": 0,
    "event": "batch_submission",
    "input_count": 5,
    "output_guesses": [
      "human",
      "human",
      "ai",
      "human",
      "human"
    ],
    "processing_ms": 0.411,
    "stage_totals_ms": {
      "combining": 0.003,
      "model": 0.001,
      "source": 0.021,
      "style": 0.048,
      "validation": 0.016
    },
    "status": "completed",
    "success_count": 5,
    "timestamp": "2026-11-18T05:29:33+00:00"
  },
  {
    "average_item_ms": 0.088,
    "batch_id": "8e27e206-68f0-4d73-9b5e-436706246408",
    "duration_ms": 0.467,
    "error_count": 0,
    "event": "batch_submission",
    "input_count": 5,
    "output_guesses": [
      "human",
      "human",
      "ai",
      "human",
      "human"
    ],
    "processing_ms": 0.44,
    "stage_totals_ms": {
      "combining": 0.003,
      "model": 0.002,
      "source": 0.021,
      "style": 0.048,
      "validation": 0.017
    },
    "status": "completed",
    "success_count": 5,
    "timestamp": "2026-11-18T05:29:33+00:00"
  },
  {
    "average_item_ms": 0.093,
    "batch_id": "199ba77d-1b73-4528-a2e8-b47789a3e7f0",
    "duration_ms": 0.485,
    "error_count": 0,
    "event": "batch_submission",
    "input_count": 5,
    "output_guesses": [
      "human",
      "human",
      "ai",
      "human",
      "human"
    ],
    "processing_ms": 0.465,
    "stage_totals_ms": {
      "combining": 0.003,
      "model": 0.001,
      "source": 0.023,
      "style": 0.05,
      "validation": 0.019
    },
    "status": "completed",
    "success_count": 5,
    "timestamp": "2026-11-18T05:29:33+00:00"
  },
  {
    "average_item_ms": 0.0,
    "batch_id": "601660ee-44ff-445f-92f7-f47a21eb97d2",
    "duration_ms": 0.034,
    "error_count": 11,
    "event": "batch_submission",
    "input_count": 11,
    "output_guesses": [],
    "rejection_reason": "batch_too_large",
    "status": "rejected",
    "success_count": 0,
    "timestamp": "2026-11-18T05:29:33+00:00"
  }
]
```

## Run Log — Before

The baseline was produced by `run_batch_eval.py::main` before model-score
caching and saved in `results/batch_eval_2026-11-17_132311_before.json`.

| Criterion | Target | Trial 1 | Trial 2 | Trial 3 | Verdict |
|---|---|---|---|---|---|
| 1. Valid batch preserves submission order | Exactly 5 results indexed 0 through 4 | 5/5, [0, 1, 2, 3, 4] — PASS | 5/5, [0, 1, 2, 3, 4] — PASS | 5/5, [0, 1, 2, 3, 4] — PASS | MET |
| 2. One invalid item does not destroy the batch | 4 successes and 1 item-level error | 4 success, 1 error — PASS | 4 success, 1 error — PASS | 4 success, 1 error — PASS | MET |
| 3. Oversized batches are rejected safely | HTTP 400, one rejection log, and 0 processed items | HTTP 400; 0 processed — PASS | HTTP 400; 0 processed — PASS | HTTP 400; 0 processed — PASS | MET |
| 4. Every completed batch is auditable | 5 decision entries and 1 batch summary | 5 decisions + 1 summary — PASS | 5 decisions + 1 summary — PASS | 5 decisions + 1 summary — PASS | MET |
| 5. Warm batch latency remains usable | Average below 100 ms per item | 14.020 ms/item — PASS | 14.003 ms/item — PASS | 14.018 ms/item — PASS | MET |

## Real Output — Before

### Criterion 1 — Valid batch preserves submission order

Produced by `run_batch_eval.py::order_trial` against `app.py::batch_submit`.

```json
[
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "5152cfa3-10b3-45b5-a660-f1ba372d9d0b",
    "result_count": 5,
    "indexes": [
      0,
      1,
      2,
      3,
      4
    ]
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "8d6e9f58-3641-48b9-b739-5a3455cb290c",
    "result_count": 5,
    "indexes": [
      0,
      1,
      2,
      3,
      4
    ]
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "126871bd-0491-4ff7-bc1b-c3d9807722e7",
    "result_count": 5,
    "indexes": [
      0,
      1,
      2,
      3,
      4
    ]
  }
]
```

### Criterion 2 — One invalid item does not destroy the batch

Produced by `run_batch_eval.py::isolation_trial` against `app.py::batch_submit`.

```json
[
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "ef669d09-3731-4ef8-a818-f64d839d6c1d",
    "success_count": 4,
    "error_count": 1,
    "error_indexes": [
      2
    ]
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "cdc7b1b4-72cb-4423-95d2-1cbcff5927d5",
    "success_count": 4,
    "error_count": 1,
    "error_indexes": [
      2
    ]
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "4f33f2c2-f7df-4743-984f-5a628e5963f8",
    "success_count": 4,
    "error_count": 1,
    "error_indexes": [
      2
    ]
  }
]
```

### Criterion 3 — Oversized batches are rejected safely

Produced by `run_batch_eval.py::oversized_trial` against `app.py::batch_submit`.

```json
[
  {
    "passed": true,
    "http_status": 400,
    "batch_id": "7c1e3b74-6c4e-40f6-bb04-ca6536aed3c6",
    "rejected_batch_entries": 1,
    "individual_entries": 0
  },
  {
    "passed": true,
    "http_status": 400,
    "batch_id": "af37ca0f-e03e-44c7-927c-44b7406b7973",
    "rejected_batch_entries": 1,
    "individual_entries": 0
  },
  {
    "passed": true,
    "http_status": 400,
    "batch_id": "6989012b-2985-4258-900d-054555462dfb",
    "rejected_batch_entries": 1,
    "individual_entries": 0
  }
]
```

### Criterion 4 — Every completed batch is auditable

Produced by `run_batch_eval.py::audit_trial` against `app.py::batch_submit`.

```json
[
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "f5a72975-956d-4dbe-b926-5288d5ec6921",
    "individual_decisions": 5,
    "batch_summaries": 1
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "36e78b9d-aae3-4430-a6d2-4ee1cfac2976",
    "individual_decisions": 5,
    "batch_summaries": 1
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "17d5c760-40d8-4687-8a82-d1afa2ae2f1b",
    "individual_decisions": 5,
    "batch_summaries": 1
  }
]
```

### Criterion 5 — Warm batch latency remains usable

Produced by `run_batch_eval.py::latency_trial` against `app.py::batch_submit`.

```json
[
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "77b1b36f-8a79-4bd7-800c-1cc9b1589791",
    "average_item_ms": 14.02,
    "duration_ms": 70.135,
    "stage_totals_ms": {
      "combining": 0.011,
      "model": 68.662,
      "source": 0.038,
      "style": 0.11,
      "validation": 0.027
    }
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "8db50403-885c-4fde-8de1-aaba52a7d714",
    "average_item_ms": 14.003,
    "duration_ms": 70.048,
    "stage_totals_ms": {
      "combining": 0.011,
      "model": 68.707,
      "source": 0.037,
      "style": 0.103,
      "validation": 0.026
    }
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "dfd2b772-ff2a-4491-af83-297495ef3caa",
    "average_item_ms": 14.018,
    "duration_ms": 70.136,
    "stage_totals_ms": {
      "combining": 0.011,
      "model": 68.73,
      "source": 0.038,
      "style": 0.105,
      "validation": 0.026
    }
  }
]
```


## Verdicts and Diagnosis

All five criteria were **MET** in all three baseline trials, so there were no
misses requiring repair. However, criterion 5's target of less than 100 ms per
warm item was too loose: the actual baseline mean was **14.014
ms/item**. A defensible tighter future target is **below 20 ms per warm item in
all three trials**. I did not edit or lower the original criterion after seeing
the results.

The timing breakdown identified a performance opportunity. Model inference
dominated warm processing, and identical submissions were recomputed even
though `model_signal` is deterministic for the same text and loaded model. A
separate cold-start observation took approximately 3.144 seconds for the first
item because it also loaded GPT-2; the next uncached warm item took about 11.4
ms. Cold start and repeated warm inference are therefore different costs.

## The Improvement

I added a bounded `functools.lru_cache(maxsize=256)` to
`detector.py::model_signal`. Repeated identical text now reuses the previously
computed model score rather than running GPT-2 inference again. I also added
cache statistics to `app.py::health` so the optimization is observable.

The change follows directly from the timing diagnosis: repeated model scoring
was the dominant avoidable stage. I reran the full five-criterion set three
times in the same format after making the change.

## Run Log — After

| Criterion | Target | Trial 1 | Trial 2 | Trial 3 | Verdict |
|---|---|---|---|---|---|
| 1. Valid batch preserves submission order | Exactly 5 results indexed 0 through 4 | 5/5, [0, 1, 2, 3, 4] — PASS | 5/5, [0, 1, 2, 3, 4] — PASS | 5/5, [0, 1, 2, 3, 4] — PASS | MET |
| 2. One invalid item does not destroy the batch | 4 successes and 1 item-level error | 4 success, 1 error — PASS | 4 success, 1 error — PASS | 4 success, 1 error — PASS | MET |
| 3. Oversized batches are rejected safely | HTTP 400, one rejection log, and 0 processed items | HTTP 400; 0 processed — PASS | HTTP 400; 0 processed — PASS | HTTP 400; 0 processed — PASS | MET |
| 4. Every completed batch is auditable | 5 decision entries and 1 batch summary | 5 decisions + 1 summary — PASS | 5 decisions + 1 summary — PASS | 5 decisions + 1 summary — PASS | MET |
| 5. Warm batch latency remains usable | Average below 100 ms per item | 0.145 ms/item — PASS | 0.127 ms/item — PASS | 0.140 ms/item — PASS | MET |

## Real Output — After

### Criterion 1 — Valid batch preserves submission order

Produced by `run_batch_eval.py::order_trial` against `app.py::batch_submit`.

```json
[
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "113e5c83-faeb-4762-bce5-1206fb58b413",
    "result_count": 5,
    "indexes": [
      0,
      1,
      2,
      3,
      4
    ]
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "9b32aebe-6495-4603-b2bb-8a9e2e64a27f",
    "result_count": 5,
    "indexes": [
      0,
      1,
      2,
      3,
      4
    ]
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "39386de4-010f-443c-800f-4cc2c2f18bd6",
    "result_count": 5,
    "indexes": [
      0,
      1,
      2,
      3,
      4
    ]
  }
]
```

### Criterion 2 — One invalid item does not destroy the batch

Produced by `run_batch_eval.py::isolation_trial` against `app.py::batch_submit`.

```json
[
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "e643c24a-503e-416c-a0d1-4939d4829c9a",
    "success_count": 4,
    "error_count": 1,
    "error_indexes": [
      2
    ]
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "786aa2df-8613-4af8-b86b-66662fb84b99",
    "success_count": 4,
    "error_count": 1,
    "error_indexes": [
      2
    ]
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "83ef7511-b493-4fb2-98b1-4eb3bf47f326",
    "success_count": 4,
    "error_count": 1,
    "error_indexes": [
      2
    ]
  }
]
```

### Criterion 3 — Oversized batches are rejected safely

Produced by `run_batch_eval.py::oversized_trial` against `app.py::batch_submit`.

```json
[
  {
    "passed": true,
    "http_status": 400,
    "batch_id": "7f38e9eb-31e0-41dc-b4ab-fdde83bf90da",
    "rejected_batch_entries": 1,
    "individual_entries": 0
  },
  {
    "passed": true,
    "http_status": 400,
    "batch_id": "151e60d8-b72e-4ecd-9447-6d22e13466a9",
    "rejected_batch_entries": 1,
    "individual_entries": 0
  },
  {
    "passed": true,
    "http_status": 400,
    "batch_id": "1fffba8f-4775-41f2-b1f2-6b582dffede3",
    "rejected_batch_entries": 1,
    "individual_entries": 0
  }
]
```

### Criterion 4 — Every completed batch is auditable

Produced by `run_batch_eval.py::audit_trial` against `app.py::batch_submit`.

```json
[
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "5f86e927-4f5c-4884-9051-b4a8829b5a4e",
    "individual_decisions": 5,
    "batch_summaries": 1
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "de5d567e-d2f1-4df0-957f-4a69f0caefe7",
    "individual_decisions": 5,
    "batch_summaries": 1
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "1ccbe997-2647-460c-8089-6a312db6b5c1",
    "individual_decisions": 5,
    "batch_summaries": 1
  }
]
```

### Criterion 5 — Warm batch latency remains usable

Produced by `run_batch_eval.py::latency_trial` against `app.py::batch_submit`.

```json
[
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "b1af1b11-4255-4cef-ba86-caa442658c46",
    "average_item_ms": 0.145,
    "duration_ms": 0.766,
    "stage_totals_ms": {
      "combining": 0.004,
      "model": 0.001,
      "source": 0.022,
      "style": 0.053,
      "validation": 0.019
    }
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "815b645d-c437-4d4b-8f5b-4b0ef6d7bcaf",
    "average_item_ms": 0.127,
    "duration_ms": 0.664,
    "stage_totals_ms": {
      "combining": 0.004,
      "model": 0.001,
      "source": 0.022,
      "style": 0.053,
      "validation": 0.019
    }
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "036e46a4-7977-4965-9ae7-6f214853cf83",
    "average_item_ms": 0.14,
    "duration_ms": 0.725,
    "stage_totals_ms": {
      "combining": 0.003,
      "model": 0.001,
      "source": 0.022,
      "style": 0.049,
      "validation": 0.019
    }
  }
]
```


### Did it help, and what did it cost elsewhere?

Yes. Mean repeated-input latency decreased from **14.014 ms/item** to
**0.137 ms/item**, a **99.0% reduction** and approximately
**102x speedup**. All five acceptance criteria remained MET in every
post-change trial, so the optimization did not break ordering, partial-error
handling, rejection, auditability, or the latency target.

The improvement applies only to identical text already present in the cache.
Unique submissions still require model inference. The cache also retains up to
256 submitted strings and scores in process memory, which creates privacy and
memory costs. It is local to one process, is not shared by multiple workers,
and disappears when the service restarts.

## What It Costs

The service uses a local model, so there is no per-request API charge. The main
measured cost is latency plus local memory. `run_batch_eval.py::latency_trial`
measured three trials after warming the model, and `app.py::batch_submit`
reported the per-item and batch durations.

For a five-item batch before caching:

```text
14.014 ms/item × 5 items = 70.068 ms/batch
70.068 ms/batch × 100 batches/day = 7006.8 ms/day
= 7.007 seconds/day
```

For a five-item batch when all five texts are already cached:

```text
0.137 ms/item × 5 items = 0.687 ms/batch
0.687 ms/batch × 100 batches/day = 68.7 ms/day
= 0.069 seconds/day
```

This is a best-case repeated-input comparison, not a promise for unique text.
The cold first request also pays several seconds to load GPT-2. Disk cost
includes the approximately 550 MB model, while runtime memory includes
PyTorch, the loaded model, Flask, and up to 256 cached text-score entries.

## What's Still Broken

No acceptance criterion remains missed, but several production limitations
remain:

- The first request after restart can take several seconds while GPT-2 loads.
- The speedup applies only to repeated identical text; unique text is uncached.
- Raw submitted text can remain temporarily in memory as an LRU-cache key.
- The JSONL audit log and verified-creator file are local rather than a
  transactional database.
- Multiple server workers would have separate caches and separate in-memory
  rate-limit state.
- Batch items are processed sequentially, not through a durable background
  queue.

Given more time, I would first replace the raw-text cache key with a bounded,
expiring content-hash cache. I would prioritize that over parallel processing
because retaining a writer's raw submission in memory creates a more important
privacy risk than the remaining warm latency creates a usability problem.

## How I Used AI — Unit 9

### Moment 1

- **What I asked for:** I asked for help turning the batch-processing idea into
  five measurable acceptance criteria and a three-trial evaluator.
- **What came back:** AI proposed tests for order preservation, partial-error
  isolation, oversized-batch rejection, audit completeness, and warm latency.
- **What I changed:** I kept targets tied to the actual ten-item route limit and
  the cost of assigning a result to the wrong writer, committed the criteria
  before the run output, and verified every target with real HTTP responses.

### Moment 2

- **What I asked for:** I asked for help interpreting the timing evidence and
  selecting a measurable improvement.
- **What came back:** AI identified repeated model inference as an avoidable
  stage and suggested a bounded score cache with observable statistics.
- **What I changed:** I limited the cache to 256 entries, exposed hits and
  misses through `/health`, reran all five criteria three times, and explicitly
  documented that the speedup applies only to repeated input and costs memory
  and privacy.

<!-- UNIT9_CAPSTONE_END -->
