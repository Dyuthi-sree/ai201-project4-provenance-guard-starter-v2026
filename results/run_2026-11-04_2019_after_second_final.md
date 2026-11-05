# Run log — after_second_final

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-04 20:19

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
    "content_id": "e8fc9e71-98c6-4493-9392-c8926053fcb5",
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
    "content_id": "efa3cb2b-baef-4552-bb11-60ee886260c5",
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
    "content_id": "42a61538-d7ec-4bb6-b590-aeaf8d9a6151",
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
    "content_id": "c5562924-8160-4090-88e7-22ce5e080a11",
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
    "content_id": "508e9578-d4d4-4654-82b2-3f0a1bfbbb0b",
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
    "content_id": "a8d6b396-5e83-4141-9af0-bc40797950e7",
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
    "content_id": "cb0e22cf-5058-4a18-b7e2-ac47b4785daa",
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
    "content_id": "15120079-c362-4caa-b54c-7b37ef52109c",
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
    "content_id": "892a709e-9354-4f60-94e4-b010fabb8296",
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
    "content_id": "e3db1eff-f3ec-4d82-a07e-d8df84ea3a2b",
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
    "content_id": "d749f22d-0d02-44ea-ae1f-117ed5b91d68",
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
    "content_id": "7e32976f-71ce-4904-b485-f8348b70556f",
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
    "content_id": "93818ed7-6b2c-435b-9b01-f945f3590e41",
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
    "content_id": "1d5e1772-2e9d-43ca-b7c8-3a136b78bd13",
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
    "content_id": "14669575-8100-4aa2-af68-779975e58cd3",
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
    "content_id": "af552456-cb9b-466d-a034-d1723e0f11eb",
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
    "content_id": "708af7bd-25a1-4b50-be7c-cd83b6e409a9",
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
    "content_id": "122f2991-d821-4fdb-a2f8-607b6036a7cd",
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
    "content_id": "790fb604-93df-459d-a260-a5eb3223df58",
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
    "content_id": "d032a13f-687e-420c-839c-7d9fa09c396b",
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
    "content_id": "8b6da798-f479-4b66-9289-4b152ad2e336",
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
    "content_id": "0b3c3e2b-a2f2-4723-b744-857b6b69a467",
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
    "content_id": "943e1878-dc53-4eef-98e3-5c618002feb8",
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
    "content_id": "b0fa5ca2-9286-4573-a6b3-393ad7dbb5a1",
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
    "content_id": "d2beccf3-4f99-4cad-9c2e-72138dfc5499",
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
    "content_id": "92784fd2-4222-4ccb-b8f9-2b8874a7c149",
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
    "content_id": "7e3146bf-6c4c-42ed-9532-44866efe8370",
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
    "content_id": "e036e0be-e4aa-484c-b97f-81457068bc2e",
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
    "content_id": "19f153ec-a1ad-47fd-a616-6aa556073c5e",
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
    "content_id": "1b0b9806-e0fd-456b-a44b-8ae41bddb2d3",
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
    "content_id": "76c2e31a-0a83-4381-b780-7a5f57a88456",
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
    "content_id": "98e426e6-f5f4-4678-a7c1-6b0364cead11",
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
    "content_id": "b9dc7c21-d820-41e7-b4e2-a6233f2f0776",
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
    "content_id": "f8fa0af0-c216-4db4-a0ed-6d257ef64de9",
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
    "content_id": "d1f4e6db-c9ce-4109-95a9-b53ec5fc713e",
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
    "content_id": "f0786442-4a51-45a8-a21e-36ddb77b3d02",
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
    "content_id": "381eec0b-98e1-4a21-9855-450ea18ba579",
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
    "content_id": "817ca169-b342-4a24-a2e2-6307b01eb53b",
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
    "content_id": "84136d4e-e0fe-41a5-9e14-2a06423aaf6b",
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
    "content_id": "a4a07240-2165-4ba7-992c-3d5d850f1303",
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
    "content_id": "2db37ca3-ccec-4d0f-98be-364a9f9276a0",
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
    "content_id": "f4227408-7e7c-47f4-bee6-647e9dfacafa",
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
    "content_id": "a0c9c2de-ddcc-410e-a741-f5ff0c81009b",
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
    "content_id": "99c3e3af-82d9-4866-976c-42fcbe10e412",
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
    "content_id": "70d37add-7cad-409d-8bc7-96731848d44e",
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
    "content_id": "fe5100a8-3982-4175-93de-7e113ace5aef",
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
    "content_id": "b032d592-6058-4f81-b27d-b715637e8180",
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
    "content_id": "780ce1d1-c30e-479b-9b5e-9e238d482462",
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
    "content_id": "a9337494-c011-492d-a776-a03857202687",
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
    "content_id": "5fc49b5d-c4e9-4282-95e5-04c25cf29118",
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
    "content_id": "5dd88aaf-d951-426c-9d8a-547218042f9a",
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
    "content_id": "22c091d1-20ae-4e3d-b85d-f6a921aa3d30",
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
    "content_id": "008790dd-b909-4920-ae1b-1d8487de6b09",
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
    "content_id": "051cce83-2837-486b-982a-58276c83107a",
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
    "content_id": "e8998758-01c4-4a19-9fac-903705af877d",
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
    "content_id": "95861777-1154-4726-a7ec-c0c1f8f58925",
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
    "content_id": "e6d68aef-e278-4d4a-ac9c-a87964f45231",
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
    "content_id": "4502dbf9-c81b-4fa8-8690-15541b2e3601",
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
    "content_id": "90aaa96d-c88b-403e-9466-24900ed5dcf0",
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
    "content_id": "3d745188-8f76-4a0b-8b02-81c57cfd00d1",
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
    "content_id": "d5ea4dcf-0f20-4217-abf3-6135b1e54174",
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
    "content_id": "333a7b01-17f7-4e4b-8a0b-efefda0427b7",
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
    "content_id": "8a6628b8-15a5-469f-80ee-de8faf2d89d1",
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
    "content_id": "72d03643-cac4-4420-82fb-2b9f12090c9f",
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
    "content_id": "da00ccf2-b96e-4e37-b22f-9499ee2246f7",
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
    "content_id": "74eb24bf-4f8f-4fd0-a06b-26f144ccf4c7",
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
    "content_id": "7ded6f2f-cbc6-43f4-b3d7-9b6a5ae99cd9",
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
    "content_id": "343dcd7f-7b75-4483-b244-1631bfe7f1ce",
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
    "content_id": "28056f7a-2a29-4a75-85cd-45789ad5e5df",
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
    "content_id": "1dfac9a1-5574-429d-bac1-21c2e54aeb39",
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
    "content_id": "cdd825e7-d86a-4d6a-af89-f12ae6281c6a",
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
    "content_id": "6c896826-cf0e-4d64-99cd-95771617ba11",
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
    "content_id": "1aa5e7f5-e7c2-41e7-bfd8-c2ec91ad38fa",
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
    "content_id": "252caac4-0871-4dfa-b84b-8a36ca8840e6",
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
    "content_id": "37dc0c90-d2ec-41de-96e9-2545c73fa982",
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
    "content_id": "5a294e94-ef21-46e7-86e6-0c2ddd912c1f",
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
    "content_id": "7edbddb3-8850-4913-9a97-3ea05079ac15",
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
    "content_id": "c640787f-d689-47c7-9ac6-9c7634f1c674",
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
    "content_id": "06fc66b9-98d4-4357-9f4e-bc0cf94f8c41",
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
    "content_id": "2d4efaea-be47-4bc3-9b1d-b33b42cd678a",
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
    "content_id": "cf3482bd-3b83-4252-95fc-4378232d641f",
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
    "content_id": "e94c250c-1301-4b4e-afa2-444819e7a540",
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
    "content_id": "e0658517-1211-4980-a208-6a0ca3df5ec7",
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
    "content_id": "ded8f901-9262-4313-878e-88515305e574",
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
