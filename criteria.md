# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. Human writing avoids high-confidence AI labels

Of 10 pieces of known human-written text, no more than 1 is labelled `high-confidence AI` in each of three trials.

**Why this target:** A false accusation can harm a real writer more than missing one AI-written submission harms the site. I allow one error because the model and style signals are imperfect, but more than one false positive out of ten would make the service unsafe for writers.

---

## 2. Clearly AI and clearly human writing have separated scores

Across at least 5 clearly AI-written samples and 5 clearly human-written samples, the average combined score for the AI samples is at least 0.20 higher than the average score for the human samples in each of three trials.

**Why this target:** The detector and style signal should create a meaningful difference between clearly different inputs. A gap smaller than 0.20 could be caused by ordinary score variation and would make the label thresholds unreliable.

---

## 3. All three labels are reachable

A test set containing clearly human, borderline, and clearly AI-written text produces at least one `high-confidence human`, one `unsure`, and one `high-confidence AI` label in each of three trials.

**Why this target:** If one label never appears, the combining weights or thresholds may make that label impossible to reach. The `unsure` label is especially important because the service should acknowledge uncertainty instead of forcing every submission into a human-or-AI judgment.

---

## 4. Every valid appeal changes status and is logged

For 5 of 5 valid appeals using an existing `content_id`, the service returns a successful response, changes the item’s status to `under_review`, and adds an appeal entry to the audit log.

**Why this target:** An appeal is the writer’s safeguard after receiving a potentially harmful label. This path uses deterministic service logic rather than model judgment, so it should work and be recorded every time.

---

## 5. Invalid submissions are rejected safely

For 5 of 5 invalid submissions—including missing text, empty text, whitespace-only text, missing `creator_id`, and text longer than 5,000 characters—the service returns HTTP 400 without calling the detector or crashing.

**Why this target:** Invalid or excessive input should be stopped before the expensive detector model runs. A 5,000-character limit allows normal submissions while reducing accidental overload and attempts to abuse the service.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
