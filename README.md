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

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
