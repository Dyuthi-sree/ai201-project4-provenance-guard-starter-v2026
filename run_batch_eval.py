#!/usr/bin/env python3
"""Run the five Unit 9 batch criteria three times and write evidence files."""

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

import requests


VALID_TEXTS = [
    "I rewrote this paragraph after comparing it carefully with my class notes.",
    "The group discussed the proposal and recorded several concerns before voting.",
    "My first attempt failed, so I changed the settings and tested the program again.",
    "The presentation explains how the sensor measures movement without taking photographs.",
    "We selected this approach because a mistaken accusation could harm a real writer.",
]


def post(session, url, path, body, timeout):
    response = session.post(f"{url}{path}", json=body, timeout=timeout)
    try:
        payload = response.json()
    except ValueError:
        payload = {"raw_response": response.text}
    return response.status_code, payload


def read_log(session, url, timeout):
    response = session.get(f"{url}/log?limit=500", timeout=timeout)
    response.raise_for_status()
    return response.json().get("entries", [])


def valid_items(prefix, count=5):
    return [
        {
            "text": VALID_TEXTS[index % len(VALID_TEXTS)],
            "creator_id": f"{prefix}_{index}",
        }
        for index in range(count)
    ]


def order_trial(session, url, trial, timeout):
    status, payload = post(
        session,
        url,
        "/batch-submit",
        {"items": valid_items(f"u9_order_t{trial}")},
        timeout,
    )
    results = payload.get("results", [])
    indexes = [item.get("index") for item in results]
    passed = (
        status == 200
        and payload.get("input_count") == 5
        and payload.get("success_count") == 5
        and indexes == [0, 1, 2, 3, 4]
    )
    return {
        "passed": passed,
        "http_status": status,
        "batch_id": payload.get("batch_id"),
        "result_count": len(results),
        "indexes": indexes,
        "response": payload,
    }


def isolation_trial(session, url, trial, timeout):
    items = valid_items(f"u9_partial_t{trial}", 4)
    items.insert(2, {"text": "   ", "creator_id": f"u9_bad_t{trial}"})
    status, payload = post(
        session, url, "/batch-submit", {"items": items}, timeout
    )
    results = payload.get("results", [])
    error_indexes = [
        item.get("index") for item in results if item.get("status") == "error"
    ]
    passed = (
        status == 200
        and payload.get("success_count") == 4
        and payload.get("error_count") == 1
        and error_indexes == [2]
    )
    return {
        "passed": passed,
        "http_status": status,
        "batch_id": payload.get("batch_id"),
        "success_count": payload.get("success_count"),
        "error_count": payload.get("error_count"),
        "error_indexes": error_indexes,
        "response": payload,
    }


def oversized_trial(session, url, trial, timeout):
    status, payload = post(
        session,
        url,
        "/batch-submit",
        {"items": valid_items(f"u9_large_t{trial}", 11)},
        timeout,
    )
    batch_id = payload.get("batch_id")
    entries = read_log(session, url, timeout)
    matching = [entry for entry in entries if entry.get("batch_id") == batch_id]
    rejection_entries = [
        entry
        for entry in matching
        if entry.get("event") == "batch_submission"
        and entry.get("status") == "rejected"
    ]
    individual_entries = [entry for entry in matching if "batch_index" in entry]
    passed = (
        status == 400
        and len(rejection_entries) == 1
        and len(individual_entries) == 0
    )
    return {
        "passed": passed,
        "http_status": status,
        "batch_id": batch_id,
        "rejected_batch_entries": len(rejection_entries),
        "individual_entries": len(individual_entries),
        "response": payload,
    }


def audit_trial(session, url, trial, timeout):
    status, payload = post(
        session,
        url,
        "/batch-submit",
        {"items": valid_items(f"u9_audit_t{trial}")},
        timeout,
    )
    batch_id = payload.get("batch_id")
    entries = read_log(session, url, timeout)
    matching = [entry for entry in entries if entry.get("batch_id") == batch_id]
    decisions = [entry for entry in matching if "batch_index" in entry]
    summaries = [
        entry for entry in matching if entry.get("event") == "batch_submission"
    ]
    passed = status == 200 and len(decisions) == 5 and len(summaries) == 1
    return {
        "passed": passed,
        "http_status": status,
        "batch_id": batch_id,
        "individual_decisions": len(decisions),
        "batch_summaries": len(summaries),
        "matching_log_entries": matching,
    }


def latency_trial(session, url, trial, timeout):
    # Warm the detector outside the measured batch.
    post(
        session,
        url,
        "/submit",
        {
            "text": "This warm-up request loads the detector before latency is measured.",
            "creator_id": f"u9_warmup_t{trial}",
        },
        timeout,
    )
    status, payload = post(
        session,
        url,
        "/batch-submit",
        {"items": valid_items(f"u9_latency_t{trial}")},
        timeout,
    )
    average = payload.get("average_item_ms")
    passed = (
        status == 200
        and isinstance(average, (int, float))
        and average < 100.0
    )
    return {
        "passed": passed,
        "http_status": status,
        "batch_id": payload.get("batch_id"),
        "average_item_ms": average,
        "duration_ms": payload.get("duration_ms"),
        "stage_totals_ms": payload.get("stage_totals_ms"),
        "response": payload,
    }


CRITERIA = [
    ("Valid batch preserves order", "5 results indexed 0–4", order_trial),
    ("Invalid item is isolated", "4 successes and 1 item error", isolation_trial),
    ("Oversized batch is rejected", "HTTP 400, logged, 0 items processed", oversized_trial),
    ("Completed batch is auditable", "5 decisions and 1 batch summary", audit_trial),
    ("Warm average latency", "Below 100 ms per item", latency_trial),
]


def summary_value(number, result):
    if number == 1:
        return f"{result['result_count']}/5; indexes {result['indexes']}"
    if number == 2:
        return f"{result['success_count']} success, {result['error_count']} error"
    if number == 3:
        return (
            f"HTTP {result['http_status']}; "
            f"{result['rejected_batch_entries']} rejection; "
            f"{result['individual_entries']} processed"
        )
    if number == 4:
        return (
            f"{result['individual_decisions']} decisions + "
            f"{result['batch_summaries']} summary"
        )
    return f"{result['average_item_ms']} ms/item"


def write_report(all_results, label, output_dir):
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    suffix = f"_{label}" if label else ""
    markdown_path = output_dir / f"batch_eval_{stamp}{suffix}.md"
    json_path = output_dir / f"batch_eval_{stamp}{suffix}.json"

    lines = [
        f"# Unit 9 Batch Evaluation{f' — {label}' if label else ''}",
        "",
        "- Produced by: `run_batch_eval.py::main`",
        "- Service route: `app.py::batch_submit`",
        "- Three trials per criterion",
        "",
        "| Criterion | Target | Trial 1 | Trial 2 | Trial 3 | Verdict |",
        "|---|---|---|---|---|---|",
    ]
    for number, (name, target, _) in enumerate(CRITERIA, 1):
        trials = all_results[str(number)]
        cells = [
            f"{summary_value(number, result)} — "
            f"{'PASS' if result['passed'] else 'FAIL'}"
            for result in trials
        ]
        verdict = "MET" if all(result["passed"] for result in trials) else "MISSED"
        lines.append(
            f"| {number}. {name} | {target} | "
            + " | ".join(cells)
            + f" | {verdict} |"
        )

    lines += ["", "## Real output", ""]
    for number, (name, _, _) in enumerate(CRITERIA, 1):
        lines += [
            f"### {number}. {name}",
            "",
            "```json",
            json.dumps(all_results[str(number)], indent=2),
            "```",
            "",
        ]

    markdown_path.write_text("\n".join(lines), encoding="utf-8")
    json_path.write_text(json.dumps(all_results, indent=2), encoding="utf-8")
    return markdown_path, json_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:5000")
    parser.add_argument("--label", default="before")
    parser.add_argument("--timeout", type=float, default=120.0)
    parser.add_argument("--trials", type=int, default=3)
    args = parser.parse_args()

    if args.trials < 3:
        sys.exit("The rubric requires at least three trials.")

    session = requests.Session()
    try:
        health = session.get(f"{args.url}/health", timeout=5)
        health.raise_for_status()
    except requests.RequestException as exc:
        sys.exit(f"Service unavailable at {args.url}: {exc}")

    all_results = {}
    for number, (name, _, function) in enumerate(CRITERIA, 1):
        print(f"\nCriterion {number}: {name}")
        trials = []
        for trial in range(1, args.trials + 1):
            result = function(session, args.url, trial, args.timeout)
            trials.append(result)
            print(
                f"  Trial {trial}: {'PASS' if result['passed'] else 'FAIL'} — "
                f"{summary_value(number, result)}"
            )
        all_results[str(number)] = trials

    output_dir = Path(__file__).resolve().parent / "results"
    output_dir.mkdir(exist_ok=True)
    markdown_path, json_path = write_report(all_results, args.label, output_dir)
    print(f"\nWrote {markdown_path}")
    print(f"Wrote {json_path}")


if __name__ == "__main__":
    main()
