# Unit 9 Batch Evaluation — before

- Produced by: `run_batch_eval.py::main`
- Service route: `app.py::batch_submit`
- Three trials per criterion

| Criterion | Target | Trial 1 | Trial 2 | Trial 3 | Verdict |
|---|---|---|---|---|---|
| 1. Valid batch preserves order | 5 results indexed 0–4 | 5/5; indexes [0, 1, 2, 3, 4] — PASS | 5/5; indexes [0, 1, 2, 3, 4] — PASS | 5/5; indexes [0, 1, 2, 3, 4] — PASS | MET |
| 2. Invalid item is isolated | 4 successes and 1 item error | 4 success, 1 error — PASS | 4 success, 1 error — PASS | 4 success, 1 error — PASS | MET |
| 3. Oversized batch is rejected | HTTP 400, logged, 0 items processed | HTTP 400; 1 rejection; 0 processed — PASS | HTTP 400; 1 rejection; 0 processed — PASS | HTTP 400; 1 rejection; 0 processed — PASS | MET |
| 4. Completed batch is auditable | 5 decisions and 1 batch summary | 5 decisions + 1 summary — PASS | 5 decisions + 1 summary — PASS | 5 decisions + 1 summary — PASS | MET |
| 5. Warm average latency | Below 100 ms per item | 14.02 ms/item — PASS | 14.003 ms/item — PASS | 14.018 ms/item — PASS | MET |

## Real output

### 1. Valid batch preserves order

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
    ],
    "response": {
      "average_item_ms": 717.339,
      "batch_id": "5152cfa3-10b3-45b5-a660-f1ba372d9d0b",
      "duration_ms": 3589.252,
      "error_count": 0,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "7ec5ddbb-aecd-4c7b-aedb-44f4a121b69e",
          "creator_credential": null,
          "creator_id": "u9_order_t1_0",
          "duration_ms": 3526.604,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 3525.949,
            "source": 0.128,
            "style": 0.205
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "3f5a816f-73b6-4c41-848a-fae555ecb977",
          "creator_credential": null,
          "creator_id": "u9_order_t1_1",
          "duration_ms": 14.304,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 14.142,
            "source": 0.008,
            "style": 0.025
          },
          "status": "success",
          "style_score": 0.6627
        },
        {
          "confidence": 0.6972,
          "content_id": "bca8d629-adb1-4b87-a787-9fda0d47e4b8",
          "creator_credential": null,
          "creator_id": "u9_order_t1_2",
          "duration_ms": 14.695,
          "guess": "ai",
          "index": 2,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 14.524,
            "source": 0.007,
            "style": 0.024
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "5356c6ed-c8c4-45c6-9b9d-f2122e3e3059",
          "creator_credential": null,
          "creator_id": "u9_order_t1_3",
          "duration_ms": 13.842,
          "guess": "human",
          "index": 3,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 13.654,
            "source": 0.008,
            "style": 0.025
          },
          "status": "success",
          "style_score": 0.667
        },
        {
          "confidence": 0.1539,
          "content_id": "224d6a02-d2a1-4029-a84d-66132e460611",
          "creator_credential": null,
          "creator_id": "u9_order_t1_4",
          "duration_ms": 16.612,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.0736,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 16.438,
            "source": 0.008,
            "style": 0.026
          },
          "status": "success",
          "style_score": 0.6638
        }
      ],
      "stage_totals_ms": {
        "combining": 0.015,
        "model": 3584.707,
        "source": 0.16,
        "style": 0.304,
        "validation": 0.034
      },
      "status": "completed",
      "success_count": 5
    }
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
    ],
    "response": {
      "average_item_ms": 14.753,
      "batch_id": "8d6e9f58-3641-48b9-b739-5a3455cb290c",
      "duration_ms": 73.812,
      "error_count": 0,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "9c547864-d504-4b0d-be40-4e86ae079464",
          "creator_credential": null,
          "creator_id": "u9_order_t2_0",
          "duration_ms": 16.495,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 16.317,
            "source": 0.008,
            "style": 0.024
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "9a3ac0fa-4e58-4e74-80ba-10bf3ba1b3dd",
          "creator_credential": null,
          "creator_id": "u9_order_t2_1",
          "duration_ms": 14.283,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 14.094,
            "source": 0.009,
            "style": 0.024
          },
          "status": "success",
          "style_score": 0.6627
        },
        {
          "confidence": 0.6972,
          "content_id": "579f5334-164e-48ff-8af2-e388dd74d336",
          "creator_credential": null,
          "creator_id": "u9_order_t2_2",
          "duration_ms": 14.511,
          "guess": "ai",
          "index": 2,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 14.326,
            "source": 0.009,
            "style": 0.027
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "b1db716f-9fb0-410e-a0b8-cc9e31710209",
          "creator_credential": null,
          "creator_id": "u9_order_t2_3",
          "duration_ms": 13.821,
          "guess": "human",
          "index": 3,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 13.664,
            "source": 0.007,
            "style": 0.021
          },
          "status": "success",
          "style_score": 0.667
        },
        {
          "confidence": 0.1539,
          "content_id": "d1809d1c-d6bf-4a44-bfc9-3f4675113a85",
          "creator_credential": null,
          "creator_id": "u9_order_t2_4",
          "duration_ms": 14.024,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.0736,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.84,
            "source": 0.008,
            "style": 0.022
          },
          "status": "success",
          "style_score": 0.6638
        }
      ],
      "stage_totals_ms": {
        "combining": 0.013,
        "model": 72.241,
        "source": 0.041,
        "style": 0.118,
        "validation": 0.032
      },
      "status": "completed",
      "success_count": 5
    }
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
    ],
    "response": {
      "average_item_ms": 14.403,
      "batch_id": "126871bd-0491-4ff7-bc1b-c3d9807722e7",
      "duration_ms": 72.052,
      "error_count": 0,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "cd3af8a7-9c4e-48f2-b9fb-48a6ca6f66dd",
          "creator_credential": null,
          "creator_id": "u9_order_t3_0",
          "duration_ms": 14.633,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 14.448,
            "source": 0.008,
            "style": 0.022
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "1f817b36-a641-4fff-b857-1af83374699e",
          "creator_credential": null,
          "creator_id": "u9_order_t3_1",
          "duration_ms": 14.857,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 14.684,
            "source": 0.007,
            "style": 0.022
          },
          "status": "success",
          "style_score": 0.6627
        },
        {
          "confidence": 0.6972,
          "content_id": "06996e99-a2b1-4dd4-8e91-a00e8e7225a9",
          "creator_credential": null,
          "creator_id": "u9_order_t3_2",
          "duration_ms": 14.34,
          "guess": "ai",
          "index": 2,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 14.164,
            "source": 0.008,
            "style": 0.023
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "dad82978-c54e-4f98-abb2-77af3d019150",
          "creator_credential": null,
          "creator_id": "u9_order_t3_3",
          "duration_ms": 13.739,
          "guess": "human",
          "index": 3,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 13.558,
            "source": 0.008,
            "style": 0.022
          },
          "status": "success",
          "style_score": 0.667
        },
        {
          "confidence": 0.1539,
          "content_id": "333b5a5e-b7b8-4820-9ede-289abf69b189",
          "creator_credential": null,
          "creator_id": "u9_order_t3_4",
          "duration_ms": 13.837,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.0736,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.678,
            "source": 0.008,
            "style": 0.021
          },
          "status": "success",
          "style_score": 0.6638
        }
      ],
      "stage_totals_ms": {
        "combining": 0.011,
        "model": 70.531,
        "source": 0.04,
        "style": 0.109,
        "validation": 0.03
      },
      "status": "completed",
      "success_count": 5
    }
  }
]
```

### 2. Invalid item is isolated

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
    ],
    "response": {
      "average_item_ms": 11.484,
      "batch_id": "ef669d09-3731-4ef8-a818-f64d839d6c1d",
      "duration_ms": 57.455,
      "error_count": 1,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "6ef29300-185a-4b04-b2bd-8d0f5d019c21",
          "creator_credential": null,
          "creator_id": "u9_partial_t1_0",
          "duration_ms": 14.955,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 14.753,
            "source": 0.008,
            "style": 0.024
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "79cc62d6-b813-4e96-b71e-c9bde25dacc4",
          "creator_credential": null,
          "creator_id": "u9_partial_t1_1",
          "duration_ms": 14.091,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.925,
            "source": 0.007,
            "style": 0.022
          },
          "status": "success",
          "style_score": 0.6627
        },
        {
          "error": "empty_text",
          "index": 2,
          "message": "The text field cannot be empty.",
          "status": "error"
        },
        {
          "confidence": 0.6972,
          "content_id": "1ce8489d-e8f7-42b6-86de-69b15119e0c2",
          "creator_credential": null,
          "creator_id": "u9_partial_t1_2",
          "duration_ms": 14.191,
          "guess": "ai",
          "index": 3,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 14.01,
            "source": 0.008,
            "style": 0.023
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "b7bd7137-fcc3-4cb4-8a03-56cb0fdcd823",
          "creator_credential": null,
          "creator_id": "u9_partial_t1_3",
          "duration_ms": 13.682,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 13.512,
            "source": 0.008,
            "style": 0.021
          },
          "status": "success",
          "style_score": 0.667
        }
      ],
      "stage_totals_ms": {
        "combining": 0.009,
        "model": 56.2,
        "source": 0.031,
        "style": 0.09,
        "validation": 0.023
      },
      "status": "partial",
      "success_count": 4
    }
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "cdc7b1b4-72cb-4423-95d2-1cbcff5927d5",
    "success_count": 4,
    "error_count": 1,
    "error_indexes": [
      2
    ],
    "response": {
      "average_item_ms": 11.385,
      "batch_id": "cdc7b1b4-72cb-4423-95d2-1cbcff5927d5",
      "duration_ms": 56.967,
      "error_count": 1,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "1ba1fbfc-a0f6-49eb-b2c1-59e263b87e24",
          "creator_credential": null,
          "creator_id": "u9_partial_t2_0",
          "duration_ms": 14.845,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 14.67,
            "source": 0.007,
            "style": 0.021
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "b04a7bf1-88ba-4901-a757-3223829fa4bc",
          "creator_credential": null,
          "creator_id": "u9_partial_t2_1",
          "duration_ms": 13.892,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.732,
            "source": 0.007,
            "style": 0.02
          },
          "status": "success",
          "style_score": 0.6627
        },
        {
          "error": "empty_text",
          "index": 2,
          "message": "The text field cannot be empty.",
          "status": "error"
        },
        {
          "confidence": 0.6972,
          "content_id": "7350bf05-d79a-4c72-9c91-ffc7e97e7bbc",
          "creator_credential": null,
          "creator_id": "u9_partial_t2_2",
          "duration_ms": 14.091,
          "guess": "ai",
          "index": 3,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.927,
            "source": 0.007,
            "style": 0.022
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "2880dd8a-6952-4626-ab3b-a330a69dfa5e",
          "creator_credential": null,
          "creator_id": "u9_partial_t2_3",
          "duration_ms": 13.654,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.494,
            "source": 0.007,
            "style": 0.02
          },
          "status": "success",
          "style_score": 0.667
        }
      ],
      "stage_totals_ms": {
        "combining": 0.008,
        "model": 55.822,
        "source": 0.029,
        "style": 0.083,
        "validation": 0.022
      },
      "status": "partial",
      "success_count": 4
    }
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "4f33f2c2-f7df-4743-984f-5a628e5963f8",
    "success_count": 4,
    "error_count": 1,
    "error_indexes": [
      2
    ],
    "response": {
      "average_item_ms": 11.282,
      "batch_id": "4f33f2c2-f7df-4743-984f-5a628e5963f8",
      "duration_ms": 56.45,
      "error_count": 1,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "2949d3e2-ad0b-486f-a9e7-b0faeb161de5",
          "creator_credential": null,
          "creator_id": "u9_partial_t3_0",
          "duration_ms": 14.434,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 14.257,
            "source": 0.008,
            "style": 0.022
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "41c86930-2edb-44ed-83c8-11ccc448a4f8",
          "creator_credential": null,
          "creator_id": "u9_partial_t3_1",
          "duration_ms": 13.774,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.615,
            "source": 0.007,
            "style": 0.021
          },
          "status": "success",
          "style_score": 0.6627
        },
        {
          "error": "empty_text",
          "index": 2,
          "message": "The text field cannot be empty.",
          "status": "error"
        },
        {
          "confidence": 0.6972,
          "content_id": "be57e7ee-2d61-4522-a825-5cefbae3984b",
          "creator_credential": null,
          "creator_id": "u9_partial_t3_2",
          "duration_ms": 14.093,
          "guess": "ai",
          "index": 3,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.918,
            "source": 0.008,
            "style": 0.024
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "fda258f9-449d-4670-9529-b4b91180656a",
          "creator_credential": null,
          "creator_id": "u9_partial_t3_3",
          "duration_ms": 13.653,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 13.486,
            "source": 0.008,
            "style": 0.022
          },
          "status": "success",
          "style_score": 0.667
        }
      ],
      "stage_totals_ms": {
        "combining": 0.009,
        "model": 55.275,
        "source": 0.031,
        "style": 0.088,
        "validation": 0.022
      },
      "status": "partial",
      "success_count": 4
    }
  }
]
```

### 3. Oversized batch is rejected

```json
[
  {
    "passed": true,
    "http_status": 400,
    "batch_id": "7c1e3b74-6c4e-40f6-bb04-ca6536aed3c6",
    "rejected_batch_entries": 1,
    "individual_entries": 0,
    "response": {
      "batch_id": "7c1e3b74-6c4e-40f6-bb04-ca6536aed3c6",
      "error": "batch_too_large",
      "message": "A batch cannot contain more than 10 submissions."
    }
  },
  {
    "passed": true,
    "http_status": 400,
    "batch_id": "af37ca0f-e03e-44c7-927c-44b7406b7973",
    "rejected_batch_entries": 1,
    "individual_entries": 0,
    "response": {
      "batch_id": "af37ca0f-e03e-44c7-927c-44b7406b7973",
      "error": "batch_too_large",
      "message": "A batch cannot contain more than 10 submissions."
    }
  },
  {
    "passed": true,
    "http_status": 400,
    "batch_id": "6989012b-2985-4258-900d-054555462dfb",
    "rejected_batch_entries": 1,
    "individual_entries": 0,
    "response": {
      "batch_id": "6989012b-2985-4258-900d-054555462dfb",
      "error": "batch_too_large",
      "message": "A batch cannot contain more than 10 submissions."
    }
  }
]
```

### 4. Completed batch is auditable

```json
[
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "f5a72975-956d-4dbe-b926-5288d5ec6921",
    "individual_decisions": 5,
    "batch_summaries": 1,
    "matching_log_entries": [
      {
        "batch_id": "f5a72975-956d-4dbe-b926-5288d5ec6921",
        "batch_index": 0,
        "combined_score": 0.2755,
        "content_id": "4a69d2f0-78e9-4b05-9f42-6909d6608ffb",
        "creator_credential": null,
        "creator_id": "u9_audit_t1_0",
        "guess": "human",
        "item_duration_ms": 15.281,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.217,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6603,
        "timestamp": "2026-11-17T19:23:11+00:00"
      },
      {
        "batch_id": "f5a72975-956d-4dbe-b926-5288d5ec6921",
        "batch_index": 1,
        "combined_score": 0.1892,
        "content_id": "a0736ed7-302d-45eb-afa0-ea53259807cb",
        "creator_credential": null,
        "creator_id": "u9_audit_t1_1",
        "guess": "human",
        "item_duration_ms": 14.188,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.1152,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6627,
        "timestamp": "2026-11-17T19:23:11+00:00"
      },
      {
        "batch_id": "f5a72975-956d-4dbe-b926-5288d5ec6921",
        "batch_index": 2,
        "combined_score": 0.6972,
        "content_id": "9174dcd6-bb78-4750-ae0b-9d0e88c55ffa",
        "creator_credential": null,
        "creator_id": "u9_audit_t1_2",
        "guess": "ai",
        "item_duration_ms": 14.247,
        "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
        "model_score": 0.7173,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6253,
        "timestamp": "2026-11-17T19:23:11+00:00"
      },
      {
        "batch_id": "f5a72975-956d-4dbe-b926-5288d5ec6921",
        "batch_index": 3,
        "combined_score": 0.2235,
        "content_id": "01a77395-ff72-4616-9a3e-33ab6e17700d",
        "creator_credential": null,
        "creator_id": "u9_audit_t1_3",
        "guess": "human",
        "item_duration_ms": 13.525,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.155,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.667,
        "timestamp": "2026-11-17T19:23:11+00:00"
      },
      {
        "batch_id": "f5a72975-956d-4dbe-b926-5288d5ec6921",
        "batch_index": 4,
        "combined_score": 0.1539,
        "content_id": "994d5f74-6bc1-4bd0-9bd8-2500191e349a",
        "creator_credential": null,
        "creator_id": "u9_audit_t1_4",
        "guess": "human",
        "item_duration_ms": 13.484,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.0736,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6638,
        "timestamp": "2026-11-17T19:23:11+00:00"
      },
      {
        "average_item_ms": 14.265,
        "batch_id": "f5a72975-956d-4dbe-b926-5288d5ec6921",
        "duration_ms": 71.359,
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
        "processing_ms": 71.324,
        "stage_totals_ms": {
          "combining": 0.012,
          "model": 69.844,
          "source": 0.041,
          "style": 0.11,
          "validation": 0.03
        },
        "status": "completed",
        "success_count": 5,
        "timestamp": "2026-11-17T19:23:11+00:00"
      }
    ]
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "36e78b9d-aae3-4430-a6d2-4ee1cfac2976",
    "individual_decisions": 5,
    "batch_summaries": 1,
    "matching_log_entries": [
      {
        "batch_id": "36e78b9d-aae3-4430-a6d2-4ee1cfac2976",
        "batch_index": 0,
        "combined_score": 0.2755,
        "content_id": "78604cfd-58b3-48f9-81f5-aa583dbe9eb5",
        "creator_credential": null,
        "creator_id": "u9_audit_t2_0",
        "guess": "human",
        "item_duration_ms": 15.425,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.217,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6603,
        "timestamp": "2026-11-17T19:23:11+00:00"
      },
      {
        "batch_id": "36e78b9d-aae3-4430-a6d2-4ee1cfac2976",
        "batch_index": 1,
        "combined_score": 0.1892,
        "content_id": "6c638361-737e-4295-b78e-d5dc17f49510",
        "creator_credential": null,
        "creator_id": "u9_audit_t2_1",
        "guess": "human",
        "item_duration_ms": 14.229,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.1152,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6627,
        "timestamp": "2026-11-17T19:23:11+00:00"
      },
      {
        "batch_id": "36e78b9d-aae3-4430-a6d2-4ee1cfac2976",
        "batch_index": 2,
        "combined_score": 0.6972,
        "content_id": "5d708aae-9679-4f52-9a39-a7e443966048",
        "creator_credential": null,
        "creator_id": "u9_audit_t2_2",
        "guess": "ai",
        "item_duration_ms": 14.111,
        "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
        "model_score": 0.7173,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6253,
        "timestamp": "2026-11-17T19:23:11+00:00"
      },
      {
        "batch_id": "36e78b9d-aae3-4430-a6d2-4ee1cfac2976",
        "batch_index": 3,
        "combined_score": 0.2235,
        "content_id": "7a3ac4a8-3954-4cca-a84c-adb7980451c1",
        "creator_credential": null,
        "creator_id": "u9_audit_t2_3",
        "guess": "human",
        "item_duration_ms": 13.646,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.155,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.667,
        "timestamp": "2026-11-17T19:23:11+00:00"
      },
      {
        "batch_id": "36e78b9d-aae3-4430-a6d2-4ee1cfac2976",
        "batch_index": 4,
        "combined_score": 0.1539,
        "content_id": "8e08ecb0-6048-4609-ab98-8bd2afbf44ae",
        "creator_credential": null,
        "creator_id": "u9_audit_t2_4",
        "guess": "human",
        "item_duration_ms": 13.676,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.0736,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6638,
        "timestamp": "2026-11-17T19:23:11+00:00"
      },
      {
        "average_item_ms": 14.333,
        "batch_id": "36e78b9d-aae3-4430-a6d2-4ee1cfac2976",
        "duration_ms": 71.701,
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
        "processing_ms": 71.663,
        "stage_totals_ms": {
          "combining": 0.01,
          "model": 70.247,
          "source": 0.038,
          "style": 0.105,
          "validation": 0.029
        },
        "status": "completed",
        "success_count": 5,
        "timestamp": "2026-11-17T19:23:11+00:00"
      }
    ]
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "17d5c760-40d8-4687-8a82-d1afa2ae2f1b",
    "individual_decisions": 5,
    "batch_summaries": 1,
    "matching_log_entries": [
      {
        "batch_id": "17d5c760-40d8-4687-8a82-d1afa2ae2f1b",
        "batch_index": 0,
        "combined_score": 0.2755,
        "content_id": "10d49359-8b29-453b-ad07-7b9a071fcf38",
        "creator_credential": null,
        "creator_id": "u9_audit_t3_0",
        "guess": "human",
        "item_duration_ms": 15.479,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.217,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6603,
        "timestamp": "2026-11-17T19:23:11+00:00"
      },
      {
        "batch_id": "17d5c760-40d8-4687-8a82-d1afa2ae2f1b",
        "batch_index": 1,
        "combined_score": 0.1892,
        "content_id": "01548bb7-8000-45f0-9c1f-2449b359baa3",
        "creator_credential": null,
        "creator_id": "u9_audit_t3_1",
        "guess": "human",
        "item_duration_ms": 13.739,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.1152,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6627,
        "timestamp": "2026-11-17T19:23:11+00:00"
      },
      {
        "batch_id": "17d5c760-40d8-4687-8a82-d1afa2ae2f1b",
        "batch_index": 2,
        "combined_score": 0.6972,
        "content_id": "0aba53aa-97a8-4768-ab39-0daa591c2257",
        "creator_credential": null,
        "creator_id": "u9_audit_t3_2",
        "guess": "ai",
        "item_duration_ms": 14.449,
        "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
        "model_score": 0.7173,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6253,
        "timestamp": "2026-11-17T19:23:11+00:00"
      },
      {
        "batch_id": "17d5c760-40d8-4687-8a82-d1afa2ae2f1b",
        "batch_index": 3,
        "combined_score": 0.2235,
        "content_id": "8877e5f3-bd79-4812-b6af-3bd544ea2320",
        "creator_credential": null,
        "creator_id": "u9_audit_t3_3",
        "guess": "human",
        "item_duration_ms": 13.842,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.155,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.667,
        "timestamp": "2026-11-17T19:23:11+00:00"
      },
      {
        "batch_id": "17d5c760-40d8-4687-8a82-d1afa2ae2f1b",
        "batch_index": 4,
        "combined_score": 0.1539,
        "content_id": "7a13397b-5570-4a14-85e2-376d4761ac09",
        "creator_credential": null,
        "creator_id": "u9_audit_t3_4",
        "guess": "human",
        "item_duration_ms": 13.796,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.0736,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6638,
        "timestamp": "2026-11-17T19:23:11+00:00"
      },
      {
        "average_item_ms": 14.382,
        "batch_id": "17d5c760-40d8-4687-8a82-d1afa2ae2f1b",
        "duration_ms": 71.945,
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
        "processing_ms": 71.91,
        "stage_totals_ms": {
          "combining": 0.011,
          "model": 70.395,
          "source": 0.039,
          "style": 0.109,
          "validation": 0.027
        },
        "status": "completed",
        "success_count": 5,
        "timestamp": "2026-11-17T19:23:11+00:00"
      }
    ]
  }
]
```

### 5. Warm average latency

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
    },
    "response": {
      "average_item_ms": 14.02,
      "batch_id": "77b1b36f-8a79-4bd7-800c-1cc9b1589791",
      "duration_ms": 70.135,
      "error_count": 0,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "c95fade3-6da5-44cc-8880-257015bbcb8f",
          "creator_credential": null,
          "creator_id": "u9_latency_t1_0",
          "duration_ms": 14.479,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 14.309,
            "source": 0.008,
            "style": 0.023
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "6fd63092-9a87-40ec-918e-201ae6801482",
          "creator_credential": null,
          "creator_id": "u9_latency_t1_1",
          "duration_ms": 13.564,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.406,
            "source": 0.007,
            "style": 0.02
          },
          "status": "success",
          "style_score": 0.6627
        },
        {
          "confidence": 0.6972,
          "content_id": "5aa9e936-aab3-4940-9a93-ccec6c31ede4",
          "creator_credential": null,
          "creator_id": "u9_latency_t1_2",
          "duration_ms": 14.043,
          "guess": "ai",
          "index": 2,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.868,
            "source": 0.008,
            "style": 0.022
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "22c72541-7c56-48de-863a-a5db814c9cfe",
          "creator_credential": null,
          "creator_id": "u9_latency_t1_3",
          "duration_ms": 13.68,
          "guess": "human",
          "index": 3,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.478,
            "source": 0.008,
            "style": 0.023
          },
          "status": "success",
          "style_score": 0.667
        },
        {
          "confidence": 0.1539,
          "content_id": "3d28200f-b75e-4016-ba0d-4972d215ba0e",
          "creator_credential": null,
          "creator_id": "u9_latency_t1_4",
          "duration_ms": 13.753,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.0736,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.601,
            "source": 0.007,
            "style": 0.021
          },
          "status": "success",
          "style_score": 0.6638
        }
      ],
      "stage_totals_ms": {
        "combining": 0.011,
        "model": 68.662,
        "source": 0.038,
        "style": 0.11,
        "validation": 0.027
      },
      "status": "completed",
      "success_count": 5
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
    },
    "response": {
      "average_item_ms": 14.003,
      "batch_id": "8db50403-885c-4fde-8de1-aaba52a7d714",
      "duration_ms": 70.048,
      "error_count": 0,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "ecdbe7f5-43b9-4bd7-bc8c-0aa0b500257e",
          "creator_credential": null,
          "creator_id": "u9_latency_t2_0",
          "duration_ms": 14.448,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 14.279,
            "source": 0.007,
            "style": 0.021
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "2988f06b-9e71-4656-97f8-d59bd1088799",
          "creator_credential": null,
          "creator_id": "u9_latency_t2_1",
          "duration_ms": 13.496,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.345,
            "source": 0.007,
            "style": 0.02
          },
          "status": "success",
          "style_score": 0.6627
        },
        {
          "confidence": 0.6972,
          "content_id": "a1985e4c-ca4b-40a4-b232-df76e8ee5fcc",
          "creator_credential": null,
          "creator_id": "u9_latency_t2_2",
          "duration_ms": 14.066,
          "guess": "ai",
          "index": 2,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.906,
            "source": 0.007,
            "style": 0.02
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "d8c46dab-43e8-4214-82eb-e51dc0616b70",
          "creator_credential": null,
          "creator_id": "u9_latency_t2_3",
          "duration_ms": 13.631,
          "guess": "human",
          "index": 3,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.485,
            "source": 0.008,
            "style": 0.021
          },
          "status": "success",
          "style_score": 0.667
        },
        {
          "confidence": 0.1539,
          "content_id": "7571156b-125b-48ba-8783-c9b1e550e15a",
          "creator_credential": null,
          "creator_id": "u9_latency_t2_4",
          "duration_ms": 13.859,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.0736,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.691,
            "source": 0.008,
            "style": 0.022
          },
          "status": "success",
          "style_score": 0.6638
        }
      ],
      "stage_totals_ms": {
        "combining": 0.011,
        "model": 68.707,
        "source": 0.037,
        "style": 0.103,
        "validation": 0.026
      },
      "status": "completed",
      "success_count": 5
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
    },
    "response": {
      "average_item_ms": 14.018,
      "batch_id": "dfd2b772-ff2a-4491-af83-297495ef3caa",
      "duration_ms": 70.136,
      "error_count": 0,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "0dd08683-c4c2-46f3-acf0-066c6e0e7433",
          "creator_credential": null,
          "creator_id": "u9_latency_t3_0",
          "duration_ms": 14.213,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 14.058,
            "source": 0.008,
            "style": 0.021
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "0fc6c3b2-62f2-45ea-be08-c65387008339",
          "creator_credential": null,
          "creator_id": "u9_latency_t3_1",
          "duration_ms": 13.609,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.455,
            "source": 0.007,
            "style": 0.02
          },
          "status": "success",
          "style_score": 0.6627
        },
        {
          "confidence": 0.6972,
          "content_id": "c4075c45-cdab-487a-bd68-6950db5b69c7",
          "creator_credential": null,
          "creator_id": "u9_latency_t3_2",
          "duration_ms": 14.039,
          "guess": "ai",
          "index": 2,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.872,
            "source": 0.008,
            "style": 0.021
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "ad95d2e9-6a25-46d0-a029-23d1cbca524f",
          "creator_credential": null,
          "creator_id": "u9_latency_t3_3",
          "duration_ms": 13.75,
          "guess": "human",
          "index": 3,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 13.605,
            "source": 0.007,
            "style": 0.02
          },
          "status": "success",
          "style_score": 0.667
        },
        {
          "confidence": 0.1539,
          "content_id": "3485ea25-e21c-4f52-9dfe-a5ddd5ba08cd",
          "creator_credential": null,
          "creator_id": "u9_latency_t3_4",
          "duration_ms": 13.91,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.0736,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.002,
            "model": 13.74,
            "source": 0.008,
            "style": 0.022
          },
          "status": "success",
          "style_score": 0.6638
        }
      ],
      "stage_totals_ms": {
        "combining": 0.011,
        "model": 68.73,
        "source": 0.038,
        "style": 0.105,
        "validation": 0.026
      },
      "status": "completed",
      "success_count": 5
    }
  }
]
```
