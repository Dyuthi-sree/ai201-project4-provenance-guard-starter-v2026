# Unit 9 Batch Evaluation — after_cache

- Produced by: `run_batch_eval.py::main`
- Service route: `app.py::batch_submit`
- Three trials per criterion

| Criterion | Target | Trial 1 | Trial 2 | Trial 3 | Verdict |
|---|---|---|---|---|---|
| 1. Valid batch preserves order | 5 results indexed 0–4 | 5/5; indexes [0, 1, 2, 3, 4] — PASS | 5/5; indexes [0, 1, 2, 3, 4] — PASS | 5/5; indexes [0, 1, 2, 3, 4] — PASS | MET |
| 2. Invalid item is isolated | 4 successes and 1 item error | 4 success, 1 error — PASS | 4 success, 1 error — PASS | 4 success, 1 error — PASS | MET |
| 3. Oversized batch is rejected | HTTP 400, logged, 0 items processed | HTTP 400; 1 rejection; 0 processed — PASS | HTTP 400; 1 rejection; 0 processed — PASS | HTTP 400; 1 rejection; 0 processed — PASS | MET |
| 4. Completed batch is auditable | 5 decisions and 1 batch summary | 5 decisions + 1 summary — PASS | 5 decisions + 1 summary — PASS | 5 decisions + 1 summary — PASS | MET |
| 5. Warm average latency | Below 100 ms per item | 0.145 ms/item — PASS | 0.127 ms/item — PASS | 0.14 ms/item — PASS | MET |

## Real output

### 1. Valid batch preserves order

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
    ],
    "response": {
      "average_item_ms": 725.629,
      "batch_id": "113e5c83-faeb-4762-bce5-1206fb58b413",
      "duration_ms": 3630.782,
      "error_count": 0,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "a98cb052-021d-4666-b4ca-ae19a8c35a5e",
          "creator_credential": null,
          "creator_id": "u9_order_t1_0",
          "duration_ms": 3569.904,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 3569.223,
            "source": 0.128,
            "style": 0.224
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "73c4654f-3fd4-4129-a881-418f3ebcb0fe",
          "creator_credential": null,
          "creator_id": "u9_order_t1_1",
          "duration_ms": 15.024,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 14.826,
            "source": 0.008,
            "style": 0.024
          },
          "status": "success",
          "style_score": 0.6627
        },
        {
          "confidence": 0.6972,
          "content_id": "c2ad0231-ee06-496a-9aa0-bfaf5777ae40",
          "creator_credential": null,
          "creator_id": "u9_order_t1_2",
          "duration_ms": 14.843,
          "guess": "ai",
          "index": 2,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 14.665,
            "source": 0.008,
            "style": 0.025
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "bbaf28d4-5487-45ef-9db8-26e86558a576",
          "creator_credential": null,
          "creator_id": "u9_order_t1_3",
          "duration_ms": 13.96,
          "guess": "human",
          "index": 3,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 13.766,
            "source": 0.008,
            "style": 0.025
          },
          "status": "success",
          "style_score": 0.667
        },
        {
          "confidence": 0.1539,
          "content_id": "27daf834-c693-4d7d-b7d3-ac18e7be0b8c",
          "creator_credential": null,
          "creator_id": "u9_order_t1_4",
          "duration_ms": 13.826,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.0736,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.003,
            "model": 13.662,
            "source": 0.008,
            "style": 0.021
          },
          "status": "success",
          "style_score": 0.6638
        }
      ],
      "stage_totals_ms": {
        "combining": 0.016,
        "model": 3626.143,
        "source": 0.161,
        "style": 0.32,
        "validation": 0.036
      },
      "status": "completed",
      "success_count": 5
    }
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
    ],
    "response": {
      "average_item_ms": 0.092,
      "batch_id": "9b32aebe-6495-4603-b2bb-8a9e2e64a27f",
      "duration_ms": 0.496,
      "error_count": 0,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "515780f1-a45c-4326-a20d-e82af2602187",
          "creator_credential": null,
          "creator_id": "u9_order_t2_0",
          "duration_ms": 0.069,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.001,
            "source": 0.006,
            "style": 0.013
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "7db8c40b-05d3-421a-a9ec-c056569674cc",
          "creator_credential": null,
          "creator_id": "u9_order_t2_1",
          "duration_ms": 0.051,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.001,
            "source": 0.004,
            "style": 0.012
          },
          "status": "success",
          "style_score": 0.6627
        },
        {
          "confidence": 0.6972,
          "content_id": "d27a2ecf-3bc4-40eb-b5c2-3c4dcf925a3c",
          "creator_credential": null,
          "creator_id": "u9_order_t2_2",
          "duration_ms": 0.049,
          "guess": "ai",
          "index": 2,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.005,
            "style": 0.013
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "699cbd6c-9861-4552-8a91-d57c7bff8822",
          "creator_credential": null,
          "creator_id": "u9_order_t2_3",
          "duration_ms": 0.039,
          "guess": "human",
          "index": 3,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.009
          },
          "status": "success",
          "style_score": 0.667
        },
        {
          "confidence": 0.1539,
          "content_id": "dcc36b1e-35f0-4d82-81ee-cead0ee58e77",
          "creator_credential": null,
          "creator_id": "u9_order_t2_4",
          "duration_ms": 0.038,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.0736,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.009
          },
          "status": "success",
          "style_score": 0.6638
        }
      ],
      "stage_totals_ms": {
        "combining": 0.005,
        "model": 0.002,
        "source": 0.022,
        "style": 0.056,
        "validation": 0.02
      },
      "status": "completed",
      "success_count": 5
    }
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
    ],
    "response": {
      "average_item_ms": 0.088,
      "batch_id": "39386de4-010f-443c-800f-4cc2c2f18bd6",
      "duration_ms": 0.47,
      "error_count": 0,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "28ed20c7-460c-447c-88bf-580ae32252a1",
          "creator_credential": null,
          "creator_id": "u9_order_t3_0",
          "duration_ms": 0.071,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.005,
            "style": 0.012
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "75f6847f-824e-4c68-b772-9a77e43631c4",
          "creator_credential": null,
          "creator_id": "u9_order_t3_1",
          "duration_ms": 0.05,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.012
          },
          "status": "success",
          "style_score": 0.6627
        },
        {
          "confidence": 0.6972,
          "content_id": "e0e266bd-c88a-4c9f-9853-42c9f64b6ca4",
          "creator_credential": null,
          "creator_id": "u9_order_t3_2",
          "duration_ms": 0.041,
          "guess": "ai",
          "index": 2,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.009
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "1af4bb0a-f6f7-4424-a3f9-dd3a60e3887a",
          "creator_credential": null,
          "creator_id": "u9_order_t3_3",
          "duration_ms": 0.037,
          "guess": "human",
          "index": 3,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.003,
            "style": 0.008
          },
          "status": "success",
          "style_score": 0.667
        },
        {
          "confidence": 0.1539,
          "content_id": "556d4f29-2007-459d-9dfa-f5c01c0eebee",
          "creator_credential": null,
          "creator_id": "u9_order_t3_4",
          "duration_ms": 0.037,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.0736,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.008
          },
          "status": "success",
          "style_score": 0.6638
        }
      ],
      "stage_totals_ms": {
        "combining": 0.003,
        "model": 0.001,
        "source": 0.02,
        "style": 0.05,
        "validation": 0.017
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
    "batch_id": "e643c24a-503e-416c-a0d1-4939d4829c9a",
    "success_count": 4,
    "error_count": 1,
    "error_indexes": [
      2
    ],
    "response": {
      "average_item_ms": 0.066,
      "batch_id": "e643c24a-503e-416c-a0d1-4939d4829c9a",
      "duration_ms": 0.354,
      "error_count": 1,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "388e4bbb-7f58-40e3-bfce-d257ee523dd6",
          "creator_credential": null,
          "creator_id": "u9_partial_t1_0",
          "duration_ms": 0.055,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.011
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "bc8d5a57-ad3b-4404-8a76-2e3a50db19cb",
          "creator_credential": null,
          "creator_id": "u9_partial_t1_1",
          "duration_ms": 0.046,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.011
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
          "content_id": "da0bb818-4a9d-41f1-a2b2-c69af1e697f9",
          "creator_credential": null,
          "creator_id": "u9_partial_t1_2",
          "duration_ms": 0.04,
          "guess": "ai",
          "index": 3,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.009
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "11b88941-6e96-4e4d-b5d6-67eb34712fb4",
          "creator_credential": null,
          "creator_id": "u9_partial_t1_3",
          "duration_ms": 0.038,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.003,
            "style": 0.008
          },
          "status": "success",
          "style_score": 0.667
        }
      ],
      "stage_totals_ms": {
        "combining": 0.003,
        "model": 0.001,
        "source": 0.016,
        "style": 0.039,
        "validation": 0.014
      },
      "status": "partial",
      "success_count": 4
    }
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "786aa2df-8613-4af8-b86b-66662fb84b99",
    "success_count": 4,
    "error_count": 1,
    "error_indexes": [
      2
    ],
    "response": {
      "average_item_ms": 0.068,
      "batch_id": "786aa2df-8613-4af8-b86b-66662fb84b99",
      "duration_ms": 0.363,
      "error_count": 1,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "44fdc227-ad03-4cd0-bf4e-a1e3b4804343",
          "creator_credential": null,
          "creator_id": "u9_partial_t2_0",
          "duration_ms": 0.048,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.01
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "e0f50428-22bd-4aa5-ab17-32790d242b1b",
          "creator_credential": null,
          "creator_id": "u9_partial_t2_1",
          "duration_ms": 0.045,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.01
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
          "content_id": "0ace8a5a-624f-4239-976d-14e1da6d0696",
          "creator_credential": null,
          "creator_id": "u9_partial_t2_2",
          "duration_ms": 0.05,
          "guess": "ai",
          "index": 3,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.005,
            "style": 0.011
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "bc2ed979-4fc3-4c33-bf54-1aa25a6ca6d1",
          "creator_credential": null,
          "creator_id": "u9_partial_t2_3",
          "duration_ms": 0.039,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.009
          },
          "status": "success",
          "style_score": 0.667
        }
      ],
      "stage_totals_ms": {
        "combining": 0.003,
        "model": 0.001,
        "source": 0.017,
        "style": 0.041,
        "validation": 0.013
      },
      "status": "partial",
      "success_count": 4
    }
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "83ef7511-b493-4fb2-98b1-4eb3bf47f326",
    "success_count": 4,
    "error_count": 1,
    "error_indexes": [
      2
    ],
    "response": {
      "average_item_ms": 0.066,
      "batch_id": "83ef7511-b493-4fb2-98b1-4eb3bf47f326",
      "duration_ms": 0.357,
      "error_count": 1,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "a71a5de0-314d-4546-bcbc-bc79545712c5",
          "creator_credential": null,
          "creator_id": "u9_partial_t3_0",
          "duration_ms": 0.057,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.005,
            "style": 0.011
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "1c767ef1-e7fe-444a-a02b-dabaa2564d8a",
          "creator_credential": null,
          "creator_id": "u9_partial_t3_1",
          "duration_ms": 0.049,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.005,
            "style": 0.012
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
          "content_id": "8a63e4b2-9c9e-4dce-bc0a-70ed60392fe4",
          "creator_credential": null,
          "creator_id": "u9_partial_t3_2",
          "duration_ms": 0.042,
          "guess": "ai",
          "index": 3,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.01
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "c8324e6b-1d8b-4c91-8b0b-25bc78e70289",
          "creator_credential": null,
          "creator_id": "u9_partial_t3_3",
          "duration_ms": 0.036,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.003,
            "style": 0.008
          },
          "status": "success",
          "style_score": 0.667
        }
      ],
      "stage_totals_ms": {
        "combining": 0.003,
        "model": 0.001,
        "source": 0.017,
        "style": 0.041,
        "validation": 0.014
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
    "batch_id": "7f38e9eb-31e0-41dc-b4ab-fdde83bf90da",
    "rejected_batch_entries": 1,
    "individual_entries": 0,
    "response": {
      "batch_id": "7f38e9eb-31e0-41dc-b4ab-fdde83bf90da",
      "error": "batch_too_large",
      "message": "A batch cannot contain more than 10 submissions."
    }
  },
  {
    "passed": true,
    "http_status": 400,
    "batch_id": "151e60d8-b72e-4ecd-9447-6d22e13466a9",
    "rejected_batch_entries": 1,
    "individual_entries": 0,
    "response": {
      "batch_id": "151e60d8-b72e-4ecd-9447-6d22e13466a9",
      "error": "batch_too_large",
      "message": "A batch cannot contain more than 10 submissions."
    }
  },
  {
    "passed": true,
    "http_status": 400,
    "batch_id": "1fffba8f-4775-41f2-b1f2-6b582dffede3",
    "rejected_batch_entries": 1,
    "individual_entries": 0,
    "response": {
      "batch_id": "1fffba8f-4775-41f2-b1f2-6b582dffede3",
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
    "batch_id": "5f86e927-4f5c-4884-9051-b4a8829b5a4e",
    "individual_decisions": 5,
    "batch_summaries": 1,
    "matching_log_entries": [
      {
        "batch_id": "5f86e927-4f5c-4884-9051-b4a8829b5a4e",
        "batch_index": 0,
        "combined_score": 0.2755,
        "content_id": "34362d40-c6eb-42b8-89b6-d7095661591b",
        "creator_credential": null,
        "creator_id": "u9_audit_t1_0",
        "guess": "human",
        "item_duration_ms": 0.07,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.217,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6603,
        "timestamp": "2026-11-17T19:31:09+00:00"
      },
      {
        "batch_id": "5f86e927-4f5c-4884-9051-b4a8829b5a4e",
        "batch_index": 1,
        "combined_score": 0.1892,
        "content_id": "55381189-1ff4-40fd-a1f4-514d9937ff64",
        "creator_credential": null,
        "creator_id": "u9_audit_t1_1",
        "guess": "human",
        "item_duration_ms": 0.044,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.1152,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6627,
        "timestamp": "2026-11-17T19:31:09+00:00"
      },
      {
        "batch_id": "5f86e927-4f5c-4884-9051-b4a8829b5a4e",
        "batch_index": 2,
        "combined_score": 0.6972,
        "content_id": "61b2d013-c7ed-4cd5-86a3-10f488ecd762",
        "creator_credential": null,
        "creator_id": "u9_audit_t1_2",
        "guess": "ai",
        "item_duration_ms": 0.038,
        "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
        "model_score": 0.7173,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6253,
        "timestamp": "2026-11-17T19:31:09+00:00"
      },
      {
        "batch_id": "5f86e927-4f5c-4884-9051-b4a8829b5a4e",
        "batch_index": 3,
        "combined_score": 0.2235,
        "content_id": "25c6385f-0cd8-47dc-a235-df298941e181",
        "creator_credential": null,
        "creator_id": "u9_audit_t1_3",
        "guess": "human",
        "item_duration_ms": 0.035,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.155,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.667,
        "timestamp": "2026-11-17T19:31:09+00:00"
      },
      {
        "batch_id": "5f86e927-4f5c-4884-9051-b4a8829b5a4e",
        "batch_index": 4,
        "combined_score": 0.1539,
        "content_id": "e2c8b023-b795-4d16-98ab-ae763725eed2",
        "creator_credential": null,
        "creator_id": "u9_audit_t1_4",
        "guess": "human",
        "item_duration_ms": 0.035,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.0736,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6638,
        "timestamp": "2026-11-17T19:31:09+00:00"
      },
      {
        "average_item_ms": 0.084,
        "batch_id": "5f86e927-4f5c-4884-9051-b4a8829b5a4e",
        "duration_ms": 0.45,
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
        "processing_ms": 0.421,
        "stage_totals_ms": {
          "combining": 0.004,
          "model": 0.003,
          "source": 0.02,
          "style": 0.049,
          "validation": 0.017
        },
        "status": "completed",
        "success_count": 5,
        "timestamp": "2026-11-17T19:31:09+00:00"
      }
    ]
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "de5d567e-d2f1-4df0-957f-4a69f0caefe7",
    "individual_decisions": 5,
    "batch_summaries": 1,
    "matching_log_entries": [
      {
        "batch_id": "de5d567e-d2f1-4df0-957f-4a69f0caefe7",
        "batch_index": 0,
        "combined_score": 0.2755,
        "content_id": "d659d3eb-0c4e-46c6-8b83-29e2b7867221",
        "creator_credential": null,
        "creator_id": "u9_audit_t2_0",
        "guess": "human",
        "item_duration_ms": 0.082,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.217,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6603,
        "timestamp": "2026-11-17T19:31:09+00:00"
      },
      {
        "batch_id": "de5d567e-d2f1-4df0-957f-4a69f0caefe7",
        "batch_index": 1,
        "combined_score": 0.1892,
        "content_id": "fa9066d1-2e64-4f48-8da6-16894dbacdce",
        "creator_credential": null,
        "creator_id": "u9_audit_t2_1",
        "guess": "human",
        "item_duration_ms": 0.045,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.1152,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6627,
        "timestamp": "2026-11-17T19:31:09+00:00"
      },
      {
        "batch_id": "de5d567e-d2f1-4df0-957f-4a69f0caefe7",
        "batch_index": 2,
        "combined_score": 0.6972,
        "content_id": "177e7fc9-0cb2-4f3e-b1df-c28c36073e9b",
        "creator_credential": null,
        "creator_id": "u9_audit_t2_2",
        "guess": "ai",
        "item_duration_ms": 0.042,
        "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
        "model_score": 0.7173,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6253,
        "timestamp": "2026-11-17T19:31:09+00:00"
      },
      {
        "batch_id": "de5d567e-d2f1-4df0-957f-4a69f0caefe7",
        "batch_index": 3,
        "combined_score": 0.2235,
        "content_id": "105c92d5-a31d-4bcc-a16e-9a553e301303",
        "creator_credential": null,
        "creator_id": "u9_audit_t2_3",
        "guess": "human",
        "item_duration_ms": 0.038,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.155,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.667,
        "timestamp": "2026-11-17T19:31:09+00:00"
      },
      {
        "batch_id": "de5d567e-d2f1-4df0-957f-4a69f0caefe7",
        "batch_index": 4,
        "combined_score": 0.1539,
        "content_id": "030f008e-af18-4d3a-9096-785bb5e977ba",
        "creator_credential": null,
        "creator_id": "u9_audit_t2_4",
        "guess": "human",
        "item_duration_ms": 0.039,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.0736,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6638,
        "timestamp": "2026-11-17T19:31:09+00:00"
      },
      {
        "average_item_ms": 0.091,
        "batch_id": "de5d567e-d2f1-4df0-957f-4a69f0caefe7",
        "duration_ms": 0.487,
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
        "processing_ms": 0.457,
        "stage_totals_ms": {
          "combining": 0.004,
          "model": 0.001,
          "source": 0.021,
          "style": 0.048,
          "validation": 0.018
        },
        "status": "completed",
        "success_count": 5,
        "timestamp": "2026-11-17T19:31:09+00:00"
      }
    ]
  },
  {
    "passed": true,
    "http_status": 200,
    "batch_id": "1ccbe997-2647-460c-8089-6a312db6b5c1",
    "individual_decisions": 5,
    "batch_summaries": 1,
    "matching_log_entries": [
      {
        "batch_id": "1ccbe997-2647-460c-8089-6a312db6b5c1",
        "batch_index": 0,
        "combined_score": 0.2755,
        "content_id": "9f6918c5-dc05-4857-ad1f-141e03bfad42",
        "creator_credential": null,
        "creator_id": "u9_audit_t3_0",
        "guess": "human",
        "item_duration_ms": 0.096,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.217,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6603,
        "timestamp": "2026-11-17T19:31:09+00:00"
      },
      {
        "batch_id": "1ccbe997-2647-460c-8089-6a312db6b5c1",
        "batch_index": 1,
        "combined_score": 0.1892,
        "content_id": "1f858793-6348-4aa5-b43e-20987f655cc2",
        "creator_credential": null,
        "creator_id": "u9_audit_t3_1",
        "guess": "human",
        "item_duration_ms": 0.19,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.1152,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6627,
        "timestamp": "2026-11-17T19:31:09+00:00"
      },
      {
        "batch_id": "1ccbe997-2647-460c-8089-6a312db6b5c1",
        "batch_index": 2,
        "combined_score": 0.6972,
        "content_id": "22f47905-ef33-443a-bd62-78cf51cdc909",
        "creator_credential": null,
        "creator_id": "u9_audit_t3_2",
        "guess": "ai",
        "item_duration_ms": 0.048,
        "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
        "model_score": 0.7173,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6253,
        "timestamp": "2026-11-17T19:31:09+00:00"
      },
      {
        "batch_id": "1ccbe997-2647-460c-8089-6a312db6b5c1",
        "batch_index": 3,
        "combined_score": 0.2235,
        "content_id": "e408778a-654a-44e9-b8da-971feac2422f",
        "creator_credential": null,
        "creator_id": "u9_audit_t3_3",
        "guess": "human",
        "item_duration_ms": 0.039,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.155,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.667,
        "timestamp": "2026-11-17T19:31:09+00:00"
      },
      {
        "batch_id": "1ccbe997-2647-460c-8089-6a312db6b5c1",
        "batch_index": 4,
        "combined_score": 0.1539,
        "content_id": "b799b2d0-44da-4862-9c71-91f701d4bed2",
        "creator_credential": null,
        "creator_id": "u9_audit_t3_4",
        "guess": "human",
        "item_duration_ms": 0.037,
        "label": "This text shows strong signals of human writing.",
        "model_score": 0.0736,
        "source_score": 0.5,
        "status": "decided",
        "style_score": 0.6638,
        "timestamp": "2026-11-17T19:31:09+00:00"
      },
      {
        "average_item_ms": 0.152,
        "batch_id": "1ccbe997-2647-460c-8089-6a312db6b5c1",
        "duration_ms": 0.802,
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
        "processing_ms": 0.758,
        "stage_totals_ms": {
          "combining": 0.007,
          "model": 0.003,
          "source": 0.035,
          "style": 0.097,
          "validation": 0.031
        },
        "status": "completed",
        "success_count": 5,
        "timestamp": "2026-11-17T19:31:09+00:00"
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
    "batch_id": "b1af1b11-4255-4cef-ba86-caa442658c46",
    "average_item_ms": 0.145,
    "duration_ms": 0.766,
    "stage_totals_ms": {
      "combining": 0.004,
      "model": 0.001,
      "source": 0.022,
      "style": 0.053,
      "validation": 0.019
    },
    "response": {
      "average_item_ms": 0.145,
      "batch_id": "b1af1b11-4255-4cef-ba86-caa442658c46",
      "duration_ms": 0.766,
      "error_count": 0,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "4a92e577-0169-44e0-9c29-e790842b39eb",
          "creator_credential": null,
          "creator_id": "u9_latency_t1_0",
          "duration_ms": 0.097,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.005,
            "style": 0.013
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "ae560c0c-67f6-4b6f-b34c-c0fed687c6ab",
          "creator_credential": null,
          "creator_id": "u9_latency_t1_1",
          "duration_ms": 0.086,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.005,
            "style": 0.012
          },
          "status": "success",
          "style_score": 0.6627
        },
        {
          "confidence": 0.6972,
          "content_id": "4bbd49ce-3040-46f9-a070-a41844650534",
          "creator_credential": null,
          "creator_id": "u9_latency_t1_2",
          "duration_ms": 0.071,
          "guess": "ai",
          "index": 2,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.01
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "9e7818a2-b16c-4e3c-9340-18f26c00b8f2",
          "creator_credential": null,
          "creator_id": "u9_latency_t1_3",
          "duration_ms": 0.058,
          "guess": "human",
          "index": 3,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.009
          },
          "status": "success",
          "style_score": 0.667
        },
        {
          "confidence": 0.1539,
          "content_id": "c7ea286c-890c-4770-805a-a1fd9baa26eb",
          "creator_credential": null,
          "creator_id": "u9_latency_t1_4",
          "duration_ms": 0.061,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.0736,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.009
          },
          "status": "success",
          "style_score": 0.6638
        }
      ],
      "stage_totals_ms": {
        "combining": 0.004,
        "model": 0.001,
        "source": 0.022,
        "style": 0.053,
        "validation": 0.019
      },
      "status": "completed",
      "success_count": 5
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
    },
    "response": {
      "average_item_ms": 0.127,
      "batch_id": "815b645d-c437-4d4b-8f5b-4b0ef6d7bcaf",
      "duration_ms": 0.664,
      "error_count": 0,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "41c9b8c2-9a81-49f3-b24d-e5d449f54681",
          "creator_credential": null,
          "creator_id": "u9_latency_t2_0",
          "duration_ms": 0.087,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.005,
            "style": 0.013
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "bce04d71-0d75-4a5b-8d27-690051e4ea43",
          "creator_credential": null,
          "creator_id": "u9_latency_t2_1",
          "duration_ms": 0.064,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.005,
            "style": 0.012
          },
          "status": "success",
          "style_score": 0.6627
        },
        {
          "confidence": 0.6972,
          "content_id": "705b152e-1bad-4dfe-a95f-c966c30af483",
          "creator_credential": null,
          "creator_id": "u9_latency_t2_2",
          "duration_ms": 0.052,
          "guess": "ai",
          "index": 2,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.01
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "d43bf5fe-5c10-4f44-ba03-4c64d92259ad",
          "creator_credential": null,
          "creator_id": "u9_latency_t2_3",
          "duration_ms": 0.06,
          "guess": "human",
          "index": 3,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.009
          },
          "status": "success",
          "style_score": 0.667
        },
        {
          "confidence": 0.1539,
          "content_id": "eba87868-ed42-43c2-8f63-ac483ba4acb9",
          "creator_credential": null,
          "creator_id": "u9_latency_t2_4",
          "duration_ms": 0.065,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.0736,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.009
          },
          "status": "success",
          "style_score": 0.6638
        }
      ],
      "stage_totals_ms": {
        "combining": 0.004,
        "model": 0.001,
        "source": 0.022,
        "style": 0.053,
        "validation": 0.019
      },
      "status": "completed",
      "success_count": 5
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
    },
    "response": {
      "average_item_ms": 0.14,
      "batch_id": "036e46a4-7977-4965-9ae7-6f214853cf83",
      "duration_ms": 0.725,
      "error_count": 0,
      "input_count": 5,
      "results": [
        {
          "confidence": 0.2755,
          "content_id": "f5c6d385-8ec6-488f-be8c-d9c69308980d",
          "creator_credential": null,
          "creator_id": "u9_latency_t3_0",
          "duration_ms": 0.076,
          "guess": "human",
          "index": 0,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.217,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.005,
            "style": 0.011
          },
          "status": "success",
          "style_score": 0.6603
        },
        {
          "confidence": 0.1892,
          "content_id": "8a62841b-a30f-4cf8-b464-bb2c904dc81d",
          "creator_credential": null,
          "creator_id": "u9_latency_t3_1",
          "duration_ms": 0.052,
          "guess": "human",
          "index": 1,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.1152,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.009
          },
          "status": "success",
          "style_score": 0.6627
        },
        {
          "confidence": 0.6972,
          "content_id": "cf6eb464-fbd3-4e08-b1da-a07d2d7c0fda",
          "creator_credential": null,
          "creator_id": "u9_latency_t3_2",
          "duration_ms": 0.064,
          "guess": "ai",
          "index": 2,
          "label": "This text shows strong signals of AI-generated writing. This automated estimate may be appealed.",
          "model_score": 0.7173,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.005,
            "style": 0.011
          },
          "status": "success",
          "style_score": 0.6253
        },
        {
          "confidence": 0.2235,
          "content_id": "0a28cf74-e4d8-4368-8e7e-a3b6bd4ce3f3",
          "creator_credential": null,
          "creator_id": "u9_latency_t3_3",
          "duration_ms": 0.066,
          "guess": "human",
          "index": 3,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.155,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.009
          },
          "status": "success",
          "style_score": 0.667
        },
        {
          "confidence": 0.1539,
          "content_id": "be8c14f3-9b5e-4b82-9080-ca1e4698b34c",
          "creator_credential": null,
          "creator_id": "u9_latency_t3_4",
          "duration_ms": 0.061,
          "guess": "human",
          "index": 4,
          "label": "This text shows strong signals of human writing.",
          "model_score": 0.0736,
          "source_score": 0.5,
          "stage_duration_ms": {
            "combining": 0.001,
            "model": 0.0,
            "source": 0.004,
            "style": 0.009
          },
          "status": "success",
          "style_score": 0.6638
        }
      ],
      "stage_totals_ms": {
        "combining": 0.003,
        "model": 0.001,
        "source": 0.022,
        "style": 0.049,
        "validation": 0.019
      },
      "status": "completed",
      "success_count": 5
    }
  }
]
```
