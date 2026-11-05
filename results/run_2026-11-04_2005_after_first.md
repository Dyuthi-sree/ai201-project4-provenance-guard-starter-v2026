# Run log — after_first

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-04 20:05

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Human writing avoids high-confidence AI labels | At most 1 of 10 labelled AI in every run | 1/10 AI — PASS | 1/10 AI — PASS | 1/10 AI — PASS | MET |
| 2. Clearly AI and clearly human writing have separated scores | AI average at least 0.20 above human average in every run | +0.2125 — PASS | +0.2125 — PASS | +0.2125 — PASS | MET |
| 3. All three labels are reachable | Human, unsure, and AI all appear in every run | 1/3 — FAIL | 1/3 — FAIL | 1/3 — FAIL | MISSED |
| 4. Every valid appeal changes status and is logged | 5 of 5 appeals under review and logged in every run | 5/5 — PASS | 5/5 — PASS | 5/5 — PASS | MET |
| 5. Invalid submissions are rejected safely | 5 of 5 return 400 without crashing in every run | 5/5 — PASS | 5/5 — PASS | 5/5 — PASS | MET |
---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### my own human writing

**Trial 1**

```json
[
  {
    "status": 200,
    "content_id": "da357e08-934b-475e-8cbe-acd1813dfba8",
    "guess": "ai",
    "confidence": 0.6542,
    "model_score": 0.6988,
    "style_score": 0.3524,
    "source_score": 0.5,
    "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
    "sent": "Obesity, body weight, and physical activity were chosen as the main re"
  },
  {
    "status": 200,
    "content_id": "63ff3c01-eae6-4f09-bb82-7b4303bbbde7",
    "guess": "unsure",
    "confidence": 0.6026,
    "model_score": 0.6228,
    "style_score": 0.4823,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The WCRF/AICR scoring system evaluates how closely a person follows ca"
  },
  {
    "status": 200,
    "content_id": "6a3c57b6-926b-44fa-9d1f-fd9638760ca8",
    "guess": "unsure",
    "confidence": 0.4503,
    "model_score": 0.4502,
    "style_score": 0.4259,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Current food-tracking technologies may be unable to distinguish foods "
  },
  {
    "status": 200,
    "content_id": "a798e552-7733-44ac-b0ba-4572aca1ff35",
    "guess": "unsure",
    "confidence": 0.3987,
    "model_score": 0.3641,
    "style_score": 0.6422,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The device includes a Time of Flight depth sensor and an Inertial Meas"
  },
  {
    "status": 200,
    "content_id": "c4495978-9e4a-4b2b-aa9b-64958e66d72a",
    "guess": "unsure",
    "confidence": 0.358,
    "model_score": 0.3294,
    "style_score": 0.5298,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The proposed system estimates energy expenditure using wearable physic"
  },
  {
    "status": 200,
    "content_id": "32bf4878-ef55-4c57-a067-e1477e366bd2",
    "guess": "human",
    "confidence": 0.2209,
    "model_score": 0.1891,
    "style_score": 0.3515,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "The presentation emphasizes the feasibility of privacy-preserving food"
  },
  {
    "status": 200,
    "content_id": "666f6974-20bf-4115-a2fb-954d1b5d35da",
    "guess": "unsure",
    "confidence": 0.5526,
    "model_score": 0.5548,
    "style_score": 0.5603,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The main objective of Aim 1 is to develop and validate the wearable AI"
  },
  {
    "status": 200,
    "content_id": "c4f43848-7f26-4068-be2f-8fe6a9924f2b",
    "guess": "unsure",
    "confidence": 0.3663,
    "model_score": 0.3443,
    "style_score": 0.4861,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Aim 2 proposes a twelve-week real-world pilot involving thirty partici"
  },
  {
    "status": 200,
    "content_id": "51c07bd9-5f2b-4ad1-8571-4d2eb853dfbf",
    "guess": "unsure",
    "confidence": 0.399,
    "model_score": 0.3968,
    "style_score": 0.3668,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Our team believes depth sensing is a useful and privacy-preserving app"
  },
  {
    "status": 200,
    "content_id": "b6fa3a5c-21be-41b4-abfa-7c0b2a871fcd",
    "guess": "unsure",
    "confidence": 0.4878,
    "model_score": 0.4937,
    "style_score": 0.4318,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Our team recommends funding the project as a pilot study with some res"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "content_id": "58f9aef3-d3bc-4351-aff1-cc6fef89dbda",
    "guess": "ai",
    "confidence": 0.6542,
    "model_score": 0.6988,
    "style_score": 0.3524,
    "source_score": 0.5,
    "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
    "sent": "Obesity, body weight, and physical activity were chosen as the main re"
  },
  {
    "status": 200,
    "content_id": "17abedd9-e02e-4ef5-aaa2-b8579a708538",
    "guess": "unsure",
    "confidence": 0.6026,
    "model_score": 0.6228,
    "style_score": 0.4823,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The WCRF/AICR scoring system evaluates how closely a person follows ca"
  },
  {
    "status": 200,
    "content_id": "e8fc820a-e42c-4448-b59b-9c97cd579ad4",
    "guess": "unsure",
    "confidence": 0.4503,
    "model_score": 0.4502,
    "style_score": 0.4259,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Current food-tracking technologies may be unable to distinguish foods "
  },
  {
    "status": 200,
    "content_id": "e3faa99d-d118-4ddb-939e-1a61cb7f8e1a",
    "guess": "unsure",
    "confidence": 0.3987,
    "model_score": 0.3641,
    "style_score": 0.6422,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The device includes a Time of Flight depth sensor and an Inertial Meas"
  },
  {
    "status": 200,
    "content_id": "d8baaf08-cfcb-4f4d-8169-f5b92944782b",
    "guess": "unsure",
    "confidence": 0.358,
    "model_score": 0.3294,
    "style_score": 0.5298,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The proposed system estimates energy expenditure using wearable physic"
  },
  {
    "status": 200,
    "content_id": "6ba7ce6d-2edc-477d-9af2-5caf8128d609",
    "guess": "human",
    "confidence": 0.2209,
    "model_score": 0.1891,
    "style_score": 0.3515,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "The presentation emphasizes the feasibility of privacy-preserving food"
  },
  {
    "status": 200,
    "content_id": "4ac26274-b8cb-4f3e-a5d0-0b4b0640d234",
    "guess": "unsure",
    "confidence": 0.5526,
    "model_score": 0.5548,
    "style_score": 0.5603,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The main objective of Aim 1 is to develop and validate the wearable AI"
  },
  {
    "status": 200,
    "content_id": "c1da87f8-3f79-4388-b534-34b682ee632f",
    "guess": "unsure",
    "confidence": 0.3663,
    "model_score": 0.3443,
    "style_score": 0.4861,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Aim 2 proposes a twelve-week real-world pilot involving thirty partici"
  },
  {
    "status": 200,
    "content_id": "1238fb68-bb00-4e18-98be-ce93ae183453",
    "guess": "unsure",
    "confidence": 0.399,
    "model_score": 0.3968,
    "style_score": 0.3668,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Our team believes depth sensing is a useful and privacy-preserving app"
  },
  {
    "status": 200,
    "content_id": "c24771c0-d986-44f9-8f63-2d34ad42b762",
    "guess": "unsure",
    "confidence": 0.4878,
    "model_score": 0.4937,
    "style_score": 0.4318,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Our team recommends funding the project as a pilot study with some res"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "content_id": "31ca74e3-974a-46d5-bd84-8233b55dcff2",
    "guess": "ai",
    "confidence": 0.6542,
    "model_score": 0.6988,
    "style_score": 0.3524,
    "source_score": 0.5,
    "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
    "sent": "Obesity, body weight, and physical activity were chosen as the main re"
  },
  {
    "status": 200,
    "content_id": "e3c4803a-9259-48c0-8515-dcc4f2421456",
    "guess": "unsure",
    "confidence": 0.6026,
    "model_score": 0.6228,
    "style_score": 0.4823,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The WCRF/AICR scoring system evaluates how closely a person follows ca"
  },
  {
    "status": 200,
    "content_id": "fb5323c7-22e0-4588-9369-5b033391a416",
    "guess": "unsure",
    "confidence": 0.4503,
    "model_score": 0.4502,
    "style_score": 0.4259,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Current food-tracking technologies may be unable to distinguish foods "
  },
  {
    "status": 200,
    "content_id": "5b95c2b8-9e42-402c-acf2-037c4dc7991d",
    "guess": "unsure",
    "confidence": 0.3987,
    "model_score": 0.3641,
    "style_score": 0.6422,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The device includes a Time of Flight depth sensor and an Inertial Meas"
  },
  {
    "status": 200,
    "content_id": "14e165fa-3412-41e0-aff8-ac509af1fe64",
    "guess": "unsure",
    "confidence": 0.358,
    "model_score": 0.3294,
    "style_score": 0.5298,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The proposed system estimates energy expenditure using wearable physic"
  },
  {
    "status": 200,
    "content_id": "fcc56d68-836d-41c4-a2c3-b6f322100d07",
    "guess": "human",
    "confidence": 0.2209,
    "model_score": 0.1891,
    "style_score": 0.3515,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "The presentation emphasizes the feasibility of privacy-preserving food"
  },
  {
    "status": 200,
    "content_id": "3239281e-a0b6-4f5a-9a7b-46ab4f4a2cfe",
    "guess": "unsure",
    "confidence": 0.5526,
    "model_score": 0.5548,
    "style_score": 0.5603,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The main objective of Aim 1 is to develop and validate the wearable AI"
  },
  {
    "status": 200,
    "content_id": "f8a615d9-17e0-43b2-a628-d5e690051c10",
    "guess": "unsure",
    "confidence": 0.3663,
    "model_score": 0.3443,
    "style_score": 0.4861,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Aim 2 proposes a twelve-week real-world pilot involving thirty partici"
  },
  {
    "status": 200,
    "content_id": "a160ccc0-7868-4732-a1eb-954c9a81c448",
    "guess": "unsure",
    "confidence": 0.399,
    "model_score": 0.3968,
    "style_score": 0.3668,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Our team believes depth sensing is a useful and privacy-preserving app"
  },
  {
    "status": 200,
    "content_id": "91abf425-f3b3-457b-88bf-22d772b60c0b",
    "guess": "unsure",
    "confidence": 0.4878,
    "model_score": 0.4937,
    "style_score": 0.4318,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Our team recommends funding the project as a pilot study with some res"
  }
]
```

### human versus AI score separation

**Trial 1**

```json
[
  {
    "status": 200,
    "content_id": "a051db6b-55f1-4ed4-9a45-221bcd5a4017",
    "guess": "unsure",
    "confidence": 0.5022,
    "model_score": 0.5036,
    "style_score": 0.4913,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Our team believes one or two personal reminders each day may help peop",
    "expected_source": "human"
  },
  {
    "status": 200,
    "content_id": "591c8bd2-2db7-4156-9711-e37d82e6099b",
    "guess": "human",
    "confidence": 0.1565,
    "model_score": 0.0981,
    "style_score": 0.4814,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "Depth sensing is useful for privacy because it can measure volume with",
    "expected_source": "human"
  },
  {
    "status": 200,
    "content_id": "f754f183-45d9-49de-bd6f-6484ce40f24f",
    "guess": "unsure",
    "confidence": 0.4837,
    "model_score": 0.4677,
    "style_score": 0.6111,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The pilot study can show whether people are willing to wear the device",
    "expected_source": "human"
  },
  {
    "status": 200,
    "content_id": "5a0f9195-4155-44c9-b298-f31b6442cb6c",
    "guess": "human",
    "confidence": 0.3201,
    "model_score": 0.289,
    "style_score": 0.4945,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "Before supporting the proposal, we would require a clear strategy for ",
    "expected_source": "human"
  },
  {
    "status": 200,
    "content_id": "91e0b90e-0cdf-4fc8-b0cb-3de450d24376",
    "guess": "unsure",
    "confidence": 0.3671,
    "model_score": 0.37,
    "style_score": 0.2757,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Thirty participants over twelve weeks is a reasonable beginning. The s",
    "expected_source": "human"
  },
  {
    "status": 200,
    "content_id": "523380b7-2852-4697-ab76-704518a7f328",
    "guess": "ai",
    "confidence": 0.6858,
    "model_score": 0.7202,
    "style_score": 0.4859,
    "source_score": 0.5,
    "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
    "sent": "The implementation of the proposed framework requires careful consider",
    "expected_source": "ai"
  },
  {
    "status": 200,
    "content_id": "99124ffd-2685-4919-aac9-f500bf0f1e90",
    "guess": "unsure",
    "confidence": 0.5942,
    "model_score": 0.6073,
    "style_score": 0.5296,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Effective communication is an essential component of organizational su",
    "expected_source": "ai"
  },
  {
    "status": 200,
    "content_id": "7e50e7b7-3352-41b0-8031-eca69e2a005c",
    "guess": "unsure",
    "confidence": 0.5047,
    "model_score": 0.5032,
    "style_score": 0.5193,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Artificial intelligence provides numerous opportunities to improve mod",
    "expected_source": "ai"
  },
  {
    "status": 200,
    "content_id": "d98499e4-864a-4570-9594-517fe8369300",
    "guess": "ai",
    "confidence": 0.6914,
    "model_score": 0.7305,
    "style_score": 0.4547,
    "source_score": 0.5,
    "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
    "sent": "Time management is important in today's fast-paced environment. Indivi",
    "expected_source": "ai"
  },
  {
    "status": 200,
    "content_id": "edbcf2b4-0bbb-4376-b8f3-cf20a8ddb3b9",
    "guess": "unsure",
    "confidence": 0.4158,
    "model_score": 0.4293,
    "style_score": 0.259,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The proposed solution offers a comprehensive and scalable approach. By",
    "expected_source": "ai"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "content_id": "f0575fe7-4e32-4aab-8161-8c7db5608660",
    "guess": "unsure",
    "confidence": 0.5022,
    "model_score": 0.5036,
    "style_score": 0.4913,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Our team believes one or two personal reminders each day may help peop",
    "expected_source": "human"
  },
  {
    "status": 200,
    "content_id": "f2f7329a-e791-4c55-9ef1-1c7d17495944",
    "guess": "human",
    "confidence": 0.1565,
    "model_score": 0.0981,
    "style_score": 0.4814,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "Depth sensing is useful for privacy because it can measure volume with",
    "expected_source": "human"
  },
  {
    "status": 200,
    "content_id": "c81681ef-ddca-4232-ba7a-b0cd8649c0b2",
    "guess": "unsure",
    "confidence": 0.4837,
    "model_score": 0.4677,
    "style_score": 0.6111,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The pilot study can show whether people are willing to wear the device",
    "expected_source": "human"
  },
  {
    "status": 200,
    "content_id": "6082cfe1-fd47-4c55-a463-5a8086169d6d",
    "guess": "human",
    "confidence": 0.3201,
    "model_score": 0.289,
    "style_score": 0.4945,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "Before supporting the proposal, we would require a clear strategy for ",
    "expected_source": "human"
  },
  {
    "status": 200,
    "content_id": "5d61d221-a4a6-4992-92eb-cb695aebb355",
    "guess": "unsure",
    "confidence": 0.3671,
    "model_score": 0.37,
    "style_score": 0.2757,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Thirty participants over twelve weeks is a reasonable beginning. The s",
    "expected_source": "human"
  },
  {
    "status": 200,
    "content_id": "5b473c60-f868-43cd-8eb6-129d457abf48",
    "guess": "ai",
    "confidence": 0.6858,
    "model_score": 0.7202,
    "style_score": 0.4859,
    "source_score": 0.5,
    "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
    "sent": "The implementation of the proposed framework requires careful consider",
    "expected_source": "ai"
  },
  {
    "status": 200,
    "content_id": "18fa96aa-0b43-4fbb-8876-39fed4e162cb",
    "guess": "unsure",
    "confidence": 0.5942,
    "model_score": 0.6073,
    "style_score": 0.5296,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Effective communication is an essential component of organizational su",
    "expected_source": "ai"
  },
  {
    "status": 200,
    "content_id": "ec770d28-90df-4fc0-a5f7-51bbaf1546e3",
    "guess": "unsure",
    "confidence": 0.5047,
    "model_score": 0.5032,
    "style_score": 0.5193,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Artificial intelligence provides numerous opportunities to improve mod",
    "expected_source": "ai"
  },
  {
    "status": 200,
    "content_id": "3a19dc80-f9cf-481a-b8f3-e64e0c736a75",
    "guess": "ai",
    "confidence": 0.6914,
    "model_score": 0.7305,
    "style_score": 0.4547,
    "source_score": 0.5,
    "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
    "sent": "Time management is important in today's fast-paced environment. Indivi",
    "expected_source": "ai"
  },
  {
    "status": 200,
    "content_id": "012579b6-44fb-47a5-9ffd-dfd8dbac8475",
    "guess": "unsure",
    "confidence": 0.4158,
    "model_score": 0.4293,
    "style_score": 0.259,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The proposed solution offers a comprehensive and scalable approach. By",
    "expected_source": "ai"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "content_id": "0d56eae0-621e-4268-a14e-c33e86adbd2a",
    "guess": "unsure",
    "confidence": 0.5022,
    "model_score": 0.5036,
    "style_score": 0.4913,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Our team believes one or two personal reminders each day may help peop",
    "expected_source": "human"
  },
  {
    "status": 200,
    "content_id": "ff18d81c-1216-4475-8b40-70534c53d18e",
    "guess": "human",
    "confidence": 0.1565,
    "model_score": 0.0981,
    "style_score": 0.4814,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "Depth sensing is useful for privacy because it can measure volume with",
    "expected_source": "human"
  },
  {
    "status": 200,
    "content_id": "7bff50a0-e2fb-472d-a0bc-922633212b55",
    "guess": "unsure",
    "confidence": 0.4837,
    "model_score": 0.4677,
    "style_score": 0.6111,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The pilot study can show whether people are willing to wear the device",
    "expected_source": "human"
  },
  {
    "status": 200,
    "content_id": "aea01df8-2e33-4345-83d8-0b9a5e9c99d9",
    "guess": "human",
    "confidence": 0.3201,
    "model_score": 0.289,
    "style_score": 0.4945,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "Before supporting the proposal, we would require a clear strategy for ",
    "expected_source": "human"
  },
  {
    "status": 200,
    "content_id": "f4768262-3bb1-45f1-8f5f-78146122e28b",
    "guess": "unsure",
    "confidence": 0.3671,
    "model_score": 0.37,
    "style_score": 0.2757,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Thirty participants over twelve weeks is a reasonable beginning. The s",
    "expected_source": "human"
  },
  {
    "status": 200,
    "content_id": "ed23d754-0a25-46e2-b8f0-9a51b20b5a29",
    "guess": "ai",
    "confidence": 0.6858,
    "model_score": 0.7202,
    "style_score": 0.4859,
    "source_score": 0.5,
    "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
    "sent": "The implementation of the proposed framework requires careful consider",
    "expected_source": "ai"
  },
  {
    "status": 200,
    "content_id": "839e6004-e9c9-44d4-a211-d6c64833275d",
    "guess": "unsure",
    "confidence": 0.5942,
    "model_score": 0.6073,
    "style_score": 0.5296,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Effective communication is an essential component of organizational su",
    "expected_source": "ai"
  },
  {
    "status": 200,
    "content_id": "f4dcd03c-387a-45db-bfac-4501b8d23016",
    "guess": "unsure",
    "confidence": 0.5047,
    "model_score": 0.5032,
    "style_score": 0.5193,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "Artificial intelligence provides numerous opportunities to improve mod",
    "expected_source": "ai"
  },
  {
    "status": 200,
    "content_id": "22bb73fa-911e-43f1-b50b-3ad57e18163d",
    "guess": "ai",
    "confidence": 0.6914,
    "model_score": 0.7305,
    "style_score": 0.4547,
    "source_score": 0.5,
    "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
    "sent": "Time management is important in today's fast-paced environment. Indivi",
    "expected_source": "ai"
  },
  {
    "status": 200,
    "content_id": "b1d3f0e2-2499-4d0f-a8ca-381c9d22870f",
    "guess": "unsure",
    "confidence": 0.4158,
    "model_score": 0.4293,
    "style_score": 0.259,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "The proposed solution offers a comprehensive and scalable approach. By",
    "expected_source": "ai"
  }
]
```

### all three labels reachable

**Trial 1**

```json
[
  {
    "status": 200,
    "content_id": "82e26246-9965-4016-a0fb-852ab1021ac4",
    "guess": "human",
    "confidence": 0.2962,
    "model_score": 0.2786,
    "style_score": 0.5942,
    "source_score": 0.0,
    "label": "This text shows strong signals of human writing.",
    "sent": "According to research published by Stanford, careful evaluation of AI ",
    "expected_guess": "human"
  },
  {
    "status": 200,
    "content_id": "ac2202d4-9428-41a5-8486-fe053d632888",
    "guess": "human",
    "confidence": 0.3247,
    "model_score": 0.3361,
    "style_score": 0.14,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "The system works well. It handles cases correctly and provides useful ",
    "expected_guess": "unsure"
  },
  {
    "status": 200,
    "content_id": "3b89e84f-f501-4692-a6c5-844d53c61c36",
    "guess": "human",
    "confidence": 0.3341,
    "model_score": 0.3052,
    "style_score": 0.4969,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "The implementation requires careful consideration of important factors",
    "expected_guess": "ai"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "content_id": "63289503-3b20-4849-9810-824f94a371c1",
    "guess": "human",
    "confidence": 0.2962,
    "model_score": 0.2786,
    "style_score": 0.5942,
    "source_score": 0.0,
    "label": "This text shows strong signals of human writing.",
    "sent": "According to research published by Stanford, careful evaluation of AI ",
    "expected_guess": "human"
  },
  {
    "status": 200,
    "content_id": "e4bce663-e7c6-4c7b-ba27-457a1f2fbe81",
    "guess": "human",
    "confidence": 0.3247,
    "model_score": 0.3361,
    "style_score": 0.14,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "The system works well. It handles cases correctly and provides useful ",
    "expected_guess": "unsure"
  },
  {
    "status": 200,
    "content_id": "bc1f65e7-5d12-4ae7-9870-105a3c440ecf",
    "guess": "human",
    "confidence": 0.3341,
    "model_score": 0.3052,
    "style_score": 0.4969,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "The implementation requires careful consideration of important factors",
    "expected_guess": "ai"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "content_id": "93111bd7-e100-4590-8a56-2d7450962cd5",
    "guess": "human",
    "confidence": 0.2962,
    "model_score": 0.2786,
    "style_score": 0.5942,
    "source_score": 0.0,
    "label": "This text shows strong signals of human writing.",
    "sent": "According to research published by Stanford, careful evaluation of AI ",
    "expected_guess": "human"
  },
  {
    "status": 200,
    "content_id": "58b82aec-a47b-420b-9181-c9e9f9ab9250",
    "guess": "human",
    "confidence": 0.3247,
    "model_score": 0.3361,
    "style_score": 0.14,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "The system works well. It handles cases correctly and provides useful ",
    "expected_guess": "unsure"
  },
  {
    "status": 200,
    "content_id": "7581b9ea-5bb1-48ad-8136-da7f34eb1fbb",
    "guess": "human",
    "confidence": 0.3341,
    "model_score": 0.3052,
    "style_score": 0.4969,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "The implementation requires careful consideration of important factors",
    "expected_guess": "ai"
  }
]
```

### appeal changes status and is logged

**Trial 1**

```json
[
  {
    "status": 200,
    "content_id": "ebc34eb8-d7a0-411a-917c-72b86dccd035",
    "guess": "human",
    "confidence": 0.2608,
    "model_score": 0.2014,
    "style_score": 0.6458,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "I wrote this paragraph while reviewing my class notes.",
    "appeal_http_status": 200,
    "appeal_status": "under_review",
    "current_status": "under_review",
    "appeal_logged": true
  },
  {
    "status": 200,
    "content_id": "a74f4b4e-e877-4097-b96a-63fa8042f87e",
    "guess": "human",
    "confidence": 0.2945,
    "model_score": 0.2404,
    "style_score": 0.652,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "This is my original explanation of the project requirements.",
    "appeal_http_status": 200,
    "appeal_status": "under_review",
    "current_status": "under_review",
    "appeal_logged": true
  },
  {
    "status": 200,
    "content_id": "326d9573-8b05-4b48-8daa-0e8be0ca7af5",
    "guess": "human",
    "confidence": 0.3054,
    "model_score": 0.2533,
    "style_score": 0.651,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "I drafted this response and revised it before submitting it.",
    "appeal_http_status": 200,
    "appeal_status": "under_review",
    "current_status": "under_review",
    "appeal_logged": true
  },
  {
    "status": 200,
    "content_id": "8544a3b8-e47d-4e4f-bf39-6be04e2fc0a1",
    "guess": "unsure",
    "confidence": 0.4412,
    "model_score": 0.4131,
    "style_score": 0.651,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "These sentences describe my own understanding of the topic.",
    "appeal_http_status": 200,
    "appeal_status": "under_review",
    "current_status": "under_review",
    "appeal_logged": true
  },
  {
    "status": 200,
    "content_id": "0e5085b3-384a-4a48-b247-be8177a88985",
    "guess": "human",
    "confidence": 0.1515,
    "model_score": 0.072,
    "style_score": 0.6527,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "I am requesting review because I wrote this submission myself.",
    "appeal_http_status": 200,
    "appeal_status": "under_review",
    "current_status": "under_review",
    "appeal_logged": true
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "content_id": "72f667aa-2721-493b-8663-9179a99ed544",
    "guess": "human",
    "confidence": 0.2608,
    "model_score": 0.2014,
    "style_score": 0.6458,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "I wrote this paragraph while reviewing my class notes.",
    "appeal_http_status": 200,
    "appeal_status": "under_review",
    "current_status": "under_review",
    "appeal_logged": true
  },
  {
    "status": 200,
    "content_id": "f8bd79c3-9093-43de-9eff-91edd9bdf1aa",
    "guess": "human",
    "confidence": 0.2945,
    "model_score": 0.2404,
    "style_score": 0.652,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "This is my original explanation of the project requirements.",
    "appeal_http_status": 200,
    "appeal_status": "under_review",
    "current_status": "under_review",
    "appeal_logged": true
  },
  {
    "status": 200,
    "content_id": "72addc8b-171e-4074-a5c6-55d348127e7f",
    "guess": "human",
    "confidence": 0.3054,
    "model_score": 0.2533,
    "style_score": 0.651,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "I drafted this response and revised it before submitting it.",
    "appeal_http_status": 200,
    "appeal_status": "under_review",
    "current_status": "under_review",
    "appeal_logged": true
  },
  {
    "status": 200,
    "content_id": "8c9cb39d-4804-4dbf-a00d-797189964c65",
    "guess": "unsure",
    "confidence": 0.4412,
    "model_score": 0.4131,
    "style_score": 0.651,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "These sentences describe my own understanding of the topic.",
    "appeal_http_status": 200,
    "appeal_status": "under_review",
    "current_status": "under_review",
    "appeal_logged": true
  },
  {
    "status": 200,
    "content_id": "1bb69b1f-91ca-45ae-9e52-c001845128c0",
    "guess": "human",
    "confidence": 0.1515,
    "model_score": 0.072,
    "style_score": 0.6527,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "I am requesting review because I wrote this submission myself.",
    "appeal_http_status": 200,
    "appeal_status": "under_review",
    "current_status": "under_review",
    "appeal_logged": true
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "content_id": "8dc40aa2-ef76-4ec8-98e7-9a6d1fa9199d",
    "guess": "human",
    "confidence": 0.2608,
    "model_score": 0.2014,
    "style_score": 0.6458,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "I wrote this paragraph while reviewing my class notes.",
    "appeal_http_status": 200,
    "appeal_status": "under_review",
    "current_status": "under_review",
    "appeal_logged": true
  },
  {
    "status": 200,
    "content_id": "a1c80065-2d81-4e93-9914-f2f4a28b0687",
    "guess": "human",
    "confidence": 0.2945,
    "model_score": 0.2404,
    "style_score": 0.652,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "This is my original explanation of the project requirements.",
    "appeal_http_status": 200,
    "appeal_status": "under_review",
    "current_status": "under_review",
    "appeal_logged": true
  },
  {
    "status": 200,
    "content_id": "9e713c4c-2db8-49f7-ae6f-c4c7de9bf202",
    "guess": "human",
    "confidence": 0.3054,
    "model_score": 0.2533,
    "style_score": 0.651,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "I drafted this response and revised it before submitting it.",
    "appeal_http_status": 200,
    "appeal_status": "under_review",
    "current_status": "under_review",
    "appeal_logged": true
  },
  {
    "status": 200,
    "content_id": "d4156280-74e8-465f-8192-9f6931b95a55",
    "guess": "unsure",
    "confidence": 0.4412,
    "model_score": 0.4131,
    "style_score": 0.651,
    "source_score": 0.5,
    "label": "The authorship of this text is uncertain. Review is recommended.",
    "sent": "These sentences describe my own understanding of the topic.",
    "appeal_http_status": 200,
    "appeal_status": "under_review",
    "current_status": "under_review",
    "appeal_logged": true
  },
  {
    "status": 200,
    "content_id": "2ed25a05-082d-44a8-8289-a36cf3e9e181",
    "guess": "human",
    "confidence": 0.1515,
    "model_score": 0.072,
    "style_score": 0.6527,
    "source_score": 0.5,
    "label": "This text shows strong signals of human writing.",
    "sent": "I am requesting review because I wrote this submission myself.",
    "appeal_http_status": 200,
    "appeal_status": "under_review",
    "current_status": "under_review",
    "appeal_logged": true
  }
]
```

### invalid submissions rejected safely

**Trial 1**

```json
[
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "source_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "source_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "source_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "source_score": null,
    "label": null,
    "sent": "{\"text\": 12345, \"creator_id\": \"eval_bad_number\"}"
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "source_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "source_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "source_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "source_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "source_score": null,
    "label": null,
    "sent": "{\"text\": 12345, \"creator_id\": \"eval_bad_number\"}"
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "source_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "source_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "source_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "source_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "source_score": null,
    "label": null,
    "sent": "{\"text\": 12345, \"creator_id\": \"eval_bad_number\"}"
  },
  {
    "status": 400,
    "content_id": null,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "source_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  }
]
```
