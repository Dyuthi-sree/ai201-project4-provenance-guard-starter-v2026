# Attack run — after_second_final

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 20:19
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `a5ddc1ba-fd69-45e6-b9a5-121ef5793930` | human | 0.220 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `1f4ae566-ff3a-4887-bbf1-e411f9152905` | unsure | 0.547 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `48b63244-6405-4cc1-b0d5-ba39fd1412c3` | unsure | 0.623 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `3b8174bf-b944-4567-baa2-9248fff92fbf` | unsure | 0.599 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `16f761ea-dacf-4cce-b562-cccc313a44ba` | human | 0.321 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c7f952b0-692c-4cdc-992b-35f587a326da` | unsure | 0.536 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `3a42ee98-1381-4a3b-8659-c7ac28b1c05a` | unsure | 0.591 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `1b4fd264-695f-47e6-ae2c-724d7455bc1c` | human | 0.276 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `a72e4798-77c5-4711-b271-1b9d81290a8e` | ai | 0.658 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `e9b0bbed-4234-4631-88b7-0c9e0b4915f3` | ai | 0.929 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `d70bc298-6916-4ea8-b071-9dfa06c9c253` | unsure | 0.594 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `75f1129e-d173-4913-95ea-659622b42247` | ai | 0.712 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `ce9b6624-2d73-4324-9c08-d6520eac0ddd` | ai | 0.762 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `70f3a4ea-8c8e-4367-bddc-13fd71d1fc42` | ai | 0.777 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `d40d4248-6d71-4cfa-a00f-99db7a4323ff` | ai | 0.767 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `5065520a-36ec-43b1-92f6-a20793ba3260` | ai | 0.813 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `300abe38-ec4e-45cb-8d3e-3229672f62de` | ai | 0.812 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `24370bb9-7b23-4884-933b-fa326443e325` | human | 0.320 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `bad412f6-639d-47ae-b2ff-3ac018efba7f` | unsure | 0.439 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `0ab22035-0450-4608-824f-3881af221ae3` | human | 0.218 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `80ca854d-23ee-4271-b7b3-3515c4e80720` | unsure | 0.573 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `49f17949-646b-4dd5-a3ac-66acd1ce35a9` | unsure | 0.490 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `8d884b43-d6df-4b60-88f3-f4d0cef726b4` | unsure | 0.591 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `f715305d-5317-487a-a293-c010fe8d10c5` | unsure | 0.543 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | `—` | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — | HELD |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `9fe62a48-87f0-447b-9f39-41b640e65980` | ai | 0.893 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `070ae0e1-0572-45f9-953a-a7dfc0793fad` | human | 0.114 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4797e7e6-e6dc-4f51-ae1c-d139a4d2a209` | human | 0.114 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `db500d14-2f69-40ae-bb32-83a4d3a044a3` | human | 0.114 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bc038d01-3ef2-4077-949f-6d0c1628ead2` | human | 0.114 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d9a49ca0-4a07-47b4-b681-d658a272fdd9` | human | 0.114 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `86bba02e-66b9-4418-a6e9-851136e264ec` | human | 0.114 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8e2e12dc-749c-45e1-89c6-773f821c0a8c` | human | 0.114 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `15dd1ec7-6c05-4f8b-acdf-41711d287232` | human | 0.114 | HELD |
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
| `malformed` | 20 | 0 | 20 |
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
  "content_id": "a5ddc1ba-fd69-45e6-b9a5-121ef5793930",
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
  "content_id": "1f4ae566-ff3a-4887-bbf1-e411f9152905",
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
  "content_id": "48b63244-6405-4cc1-b0d5-ba39fd1412c3",
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
  "content_id": "3b8174bf-b944-4567-baa2-9248fff92fbf",
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
  "content_id": "16f761ea-dacf-4cce-b562-cccc313a44ba",
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
  "content_id": "c7f952b0-692c-4cdc-992b-35f587a326da",
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
  "content_id": "3a42ee98-1381-4a3b-8659-c7ac28b1c05a",
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
  "content_id": "1b4fd264-695f-47e6-ae2c-724d7455bc1c",
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
  "content_id": "a72e4798-77c5-4711-b271-1b9d81290a8e",
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
  "content_id": "e9b0bbed-4234-4631-88b7-0c9e0b4915f3",
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
  "content_id": "d70bc298-6916-4ea8-b071-9dfa06c9c253",
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
  "content_id": "75f1129e-d173-4913-95ea-659622b42247",
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
  "content_id": "ce9b6624-2d73-4324-9c08-d6520eac0ddd",
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
  "content_id": "70f3a4ea-8c8e-4367-bddc-13fd71d1fc42",
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
  "content_id": "d40d4248-6d71-4cfa-a00f-99db7a4323ff",
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
  "content_id": "5065520a-36ec-43b1-92f6-a20793ba3260",
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
  "content_id": "300abe38-ec4e-45cb-8d3e-3229672f62de",
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
  "content_id": "24370bb9-7b23-4884-933b-fa326443e325",
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
  "content_id": "bad412f6-639d-47ae-b2ff-3ac018efba7f",
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
  "content_id": "0ab22035-0450-4608-824f-3881af221ae3",
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
  "content_id": "80ca854d-23ee-4271-b7b3-3515c4e80720",
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
  "content_id": "49f17949-646b-4dd5-a3ac-66acd1ce35a9",
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
  "content_id": "8d884b43-d6df-4b60-88f3-f4d0cef726b4",
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
  "content_id": "f715305d-5317-487a-a293-c010fe8d10c5",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "9fe62a48-87f0-447b-9f39-41b640e65980",
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
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "status": 429,
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
  "content_id": "070ae0e1-0572-45f9-953a-a7dfc0793fad",
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
  "content_id": "4797e7e6-e6dc-4f51-ae1c-d139a4d2a209",
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
  "content_id": "db500d14-2f69-40ae-bb32-83a4d3a044a3",
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
  "content_id": "bc038d01-3ef2-4077-949f-6d0c1628ead2",
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
  "content_id": "d9a49ca0-4a07-47b4-b681-d658a272fdd9",
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
  "content_id": "86bba02e-66b9-4418-a6e9-851136e264ec",
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
  "content_id": "8e2e12dc-749c-45e1-89c6-773f821c0a8c",
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
  "content_id": "15dd1ec7-6c05-4f8b-acdf-41711d287232",
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
