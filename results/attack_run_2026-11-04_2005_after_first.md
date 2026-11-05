# Attack run — after_first

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 20:05
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `4350c887-8640-49f0-81c9-d396408a5008` | human | 0.220 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `a90a4145-01c1-4648-9da8-d7aedf5222b9` | unsure | 0.547 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `de618a81-ca5f-4a61-8f78-c90acb16aae6` | unsure | 0.623 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `60722bbc-c644-4879-bec3-65be2c4a699d` | unsure | 0.599 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `2a898c38-5f36-4027-bdc7-dfb5d860aa3a` | human | 0.321 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `2d07d8b2-a6f3-4f13-bb4d-84f5cec9a17d` | unsure | 0.536 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `4448e2fe-9d8c-48ba-878b-3e7c1c2b91d7` | unsure | 0.591 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `163076fc-04da-46df-bb55-7b38501cd701` | human | 0.276 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `01ae956a-2cf9-49e3-bc26-519ffa9033c3` | ai | 0.658 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `6cadd0c6-6cc4-407c-898a-22ffdd514c31` | ai | 0.929 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `2d67d6f6-8bad-4f4e-b668-5d6881f1aade` | unsure | 0.594 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `eeea4243-e860-4e53-9d4d-2c8c8c88cb23` | ai | 0.712 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `f3e6f1ec-704f-45e0-bbb1-87edfcef273b` | ai | 0.762 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `6f39383f-0abc-4a85-9d93-6f5c82631501` | ai | 0.777 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `b011685d-b15a-4516-beca-a863791efc50` | ai | 0.767 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `485db9cb-5596-4446-b8a5-0663f453ec1c` | ai | 0.813 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `3b056f21-9654-4752-add9-5bebb701a4fe` | ai | 0.812 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `72b6b776-ad1e-4899-93ad-e981b56f8950` | human | 0.320 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `f32009e3-ecd3-454b-81b5-2b736750a57a` | unsure | 0.439 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `b9e8602e-4edd-460c-9af9-395a15a18135` | human | 0.218 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `9c8898d8-bb89-4752-aeea-29b821be2fb7` | unsure | 0.573 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `68c1803a-7fb7-44b4-b913-5ea06d2acb78` | unsure | 0.490 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `24ce1795-797d-4c78-8fd0-864c633ca31a` | unsure | 0.591 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `264b13dc-144a-49a0-834d-023597cb405e` | unsure | 0.543 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `b2c4a6f8-2e78-48bf-9b80-46912e6f4dc4` | human | 0.095 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `cc46ddae-2b0f-4bc6-9d32-85f64a2ef925` | human | 0.115 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `ee49eac3-156b-43bf-b97d-9e2affdfdaaa` | ai | 0.943 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `47b44acc-a665-4666-a199-04ba339c6df9` | ai | 0.972 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `9b76e2eb-5dc3-4cb1-ad83-f00ef099c9d6` | ai | 0.893 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `5057b0f7-13ec-4bc3-983b-f9e1b35bd603` | human | 0.293 | BROKE |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `4b1dd20a-5ad7-4d7a-b261-4b895330f3de` | human | 0.121 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6f9514c6-6dcd-422d-bad9-a9894c36db45` | human | 0.114 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `67920542-a5e9-458a-8447-0dfd8236d96e` | human | 0.114 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7a93666d-e5b2-478a-a103-182db3633654` | human | 0.114 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b0627cc0-4f66-4a8c-8604-2fadd09aff70` | human | 0.114 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `542209a6-d5e3-4e2f-a3af-494aaccec818` | human | 0.114 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ea5aca37-888b-45b0-b53f-a4250cd85197` | human | 0.114 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c1cf8d82-2209-486a-a68e-31e94f58b2c5` | human | 0.114 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bc1d1ae8-9ea9-40e2-82ab-f3f295eac0e4` | human | 0.114 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "4350c887-8640-49f0-81c9-d396408a5008",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.2201,
  "model_score": 0.1635,
  "style_score": 0.5609,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "a90a4145-01c1-4648-9da8-d7aedf5222b9",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5474,
  "model_score": 0.5943,
  "style_score": 0.1723,
  "label": "The authorship of this text is uncertain. Review is recommended.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "de618a81-ca5f-4a61-8f78-c90acb16aae6",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.6229,
  "model_score": 0.6662,
  "style_score": 0.3667,
  "label": "The authorship of this text is uncertain. Review is recommended.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "60722bbc-c644-4879-bec3-65be2c4a699d",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5994,
  "model_score": 0.6114,
  "style_score": 0.547,
  "label": "The authorship of this text is uncertain. Review is recommended.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "2a898c38-5f36-4027-bdc7-dfb5d860aa3a",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.321,
  "model_score": 0.3212,
  "style_score": 0.2296,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "2d07d8b2-a6f3-4f13-bb4d-84f5cec9a17d",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5363,
  "model_score": 0.5727,
  "style_score": 0.2453,
  "label": "The authorship of this text is uncertain. Review is recommended.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "4448e2fe-9d8c-48ba-878b-3e7c1c2b91d7",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5914,
  "model_score": 0.5862,
  "style_score": 0.6809,
  "label": "The authorship of this text is uncertain. Review is recommended.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "163076fc-04da-46df-bb55-7b38501cd701",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.2756,
  "model_score": 0.2452,
  "style_score": 0.4222,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "01ae956a-2cf9-49e3-bc26-519ffa9033c3",
  "creator_id": "attacker_EV09",
  "guess": "ai",
  "confidence": 0.6581,
  "model_score": 0.7042,
  "style_score": 0.3452,
  "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "6cadd0c6-6cc4-407c-898a-22ffdd514c31",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9294,
  "model_score": 0.9792,
  "style_score": 0.7211,
  "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "2d67d6f6-8bad-4f4e-b668-5d6881f1aade",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5943,
  "model_score": 0.6175,
  "style_score": 0.4446,
  "label": "The authorship of this text is uncertain. Review is recommended.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "eeea4243-e860-4e53-9d4d-2c8c8c88cb23",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7122,
  "model_score": 0.7387,
  "style_score": 0.5934,
  "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "f3e6f1ec-704f-45e0-bbb1-87edfcef273b",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7619,
  "model_score": 0.8051,
  "style_score": 0.5258,
  "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "6f39383f-0abc-4a85-9d93-6f5c82631501",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7775,
  "model_score": 0.8329,
  "style_score": 0.4455,
  "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "b011685d-b15a-4516-beca-a863791efc50",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7672,
  "model_score": 0.8005,
  "style_score": 0.6173,
  "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "485db9cb-5596-4446-b8a5-0663f453ec1c",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.8126,
  "model_score": 0.8814,
  "style_score": 0.3839,
  "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "3b056f21-9654-4752-add9-5bebb701a4fe",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.8116,
  "model_score": 0.8816,
  "style_score": 0.3728,
  "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "72b6b776-ad1e-4899-93ad-e981b56f8950",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.3201,
  "model_score": 0.3223,
  "style_score": 0.2113,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "f32009e3-ecd3-454b-81b5-2b736750a57a",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4394,
  "model_score": 0.4625,
  "style_score": 0.2129,
  "label": "The authorship of this text is uncertain. Review is recommended.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "b9e8602e-4edd-460c-9af9-395a15a18135",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2181,
  "model_score": 0.2044,
  "style_score": 0.194,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "9c8898d8-bb89-4752-aeea-29b821be2fb7",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5734,
  "model_score": 0.5943,
  "style_score": 0.4325,
  "label": "The authorship of this text is uncertain. Review is recommended.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "68c1803a-7fb7-44b4-b913-5ea06d2acb78",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.49,
  "model_score": 0.4998,
  "style_score": 0.4014,
  "label": "The authorship of this text is uncertain. Review is recommended.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "24ce1795-797d-4c78-8fd0-864c633ca31a",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5906,
  "model_score": 0.6401,
  "style_score": 0.2647,
  "label": "The authorship of this text is uncertain. Review is recommended.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "264b13dc-144a-49a0-834d-023597cb405e",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5434,
  "model_score": 0.5583,
  "style_score": 0.4385,
  "label": "The authorship of this text is uncertain. Review is recommended.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "b2c4a6f8-2e78-48bf-9b80-46912e6f4dc4",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.095,
  "model_score": 0.0,
  "style_score": 0.7,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "cc46ddae-2b0f-4bc6-9d32-85f64a2ef925",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.1145,
  "model_score": 0.0112,
  "style_score": 0.8,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "ee49eac3-156b-43bf-b97d-9e2affdfdaaa",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.943,
  "model_score": 0.9976,
  "style_score": 0.7,
  "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "47b44acc-a665-4666-a199-04ba339c6df9",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9724,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "9b76e2eb-5dc3-4cb1-ad83-f00ef099c9d6",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.8926,
  "model_score": 0.9064,
  "style_score": 0.972,
  "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "5057b0f7-13ec-4bc3-983b-f9e1b35bd603",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.293,
  "model_score": 0.2395,
  "style_score": 0.6445,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "4b1dd20a-5ad7-4d7a-b261-4b895330f3de",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.1212,
  "model_score": 0.0492,
  "style_score": 0.5437,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "6f9514c6-6dcd-422d-bad9-a9894c36db45",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1141,
  "model_score": 0.0287,
  "style_score": 0.6467,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "67920542-a5e9-458a-8447-0dfd8236d96e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1141,
  "model_score": 0.0287,
  "style_score": 0.6467,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "7a93666d-e5b2-478a-a103-182db3633654",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1141,
  "model_score": 0.0287,
  "style_score": 0.6467,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "b0627cc0-4f66-4a8c-8604-2fadd09aff70",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1141,
  "model_score": 0.0287,
  "style_score": 0.6467,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "542209a6-d5e3-4e2f-a3af-494aaccec818",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1141,
  "model_score": 0.0287,
  "style_score": 0.6467,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "ea5aca37-888b-45b0-b53f-a4250cd85197",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1141,
  "model_score": 0.0287,
  "style_score": 0.6467,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "c1cf8d82-2209-486a-a68e-31e94f58b2c5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1141,
  "model_score": 0.0287,
  "style_score": 0.6467,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "bc1d1ae8-9ea9-40e2-82ab-f3f295eac0e4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1141,
  "model_score": 0.0287,
  "style_score": 0.6467,
  "label": "This text shows strong signals of human writing.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
