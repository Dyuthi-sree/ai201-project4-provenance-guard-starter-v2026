"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own human writing",
        "criterion": 1,
        "texts": [
            (
                "Obesity, body weight, and physical activity were chosen as the "
                "main research topics because they are factors people may change "
                "to reduce their cancer risks. Body weight is associated with "
                "thirteen kinds of cancer. The proposed system is intended to "
                "promote healthier habits, including eating more plant-based "
                "food, consuming fewer sugary drinks and processed meats, and "
                "increasing physical activity."
            ),
            (
                "The WCRF/AICR scoring system evaluates how closely a person "
                "follows cancer-prevention recommendations. It evaluates healthy "
                "weight, physical activity, plant-based foods, processed foods, "
                "red and processed meats, sugary drinks, and alcohol. People "
                "with higher scores follow the recommendations more closely. "
                "The proposed system uses several of these recommendations to "
                "provide personal advice about diet and activity."
            ),
            (
                "Current food-tracking technologies may be unable to distinguish "
                "foods accurately or estimate portions and the amount consumed. "
                "Camera-based technologies may also create privacy concerns. "
                "Estimates of calories burned can be inaccurate because metabolism "
                "and physical activity differ between individuals. The proposed "
                "system addresses these problems with depth sensing, user "
                "confirmation of food types, movement tracking, and measurement "
                "of resting metabolic rate."
            ),
            (
                "The device includes a Time of Flight depth sensor and an Inertial "
                "Measurement Unit. The depth sensor estimates food portions using "
                "volume measurements without regularly capturing color images. "
                "The IMU detects body movements used to estimate physical activity "
                "and calorie consumption. These choices are intended to preserve "
                "privacy and make the device more comfortable for everyday use."
            ),
            (
                "The proposed system estimates energy expenditure using wearable "
                "physical-activity measurements and a personalized metabolic model. "
                "Resting metabolic rate is measured to calibrate the model for each "
                "participant. This personalization should produce more realistic "
                "estimates of energy expenditure and energy balance than relying "
                "on one general estimate for everyone."
            ),
            (
                "The presentation emphasizes the feasibility of privacy-preserving "
                "food measurement, wearable activity monitoring, and personalized "
                "energy-expenditure estimation. Previous research supports the "
                "development of the integrated system. However, specific numerical "
                "performance results were not visible in the supplied screenshots, "
                "so exact accuracy percentages cannot be reported reliably from "
                "the available material."
            ),
            (
                "The main objective of Aim 1 is to develop and validate the wearable "
                "AI system. Researchers plan to determine whether it can measure food "
                "portions, estimate dietary intake, monitor physical activity, and "
                "calculate energy expenditure. Its measurements should be compared "
                "with suitable reference measurements, and the system should also "
                "be evaluated for reliability, usability, and privacy."
            ),
            (
                "Aim 2 proposes a twelve-week real-world pilot involving thirty "
                "participants. Its purpose is to evaluate whether the wearable "
                "system is practical and acceptable for daily use and whether "
                "participants can follow its recommendations. The proposal compares "
                "people receiving personalized wearable-informed feedback with a "
                "group receiving less personalized guidance."
            ),
            (
                "Our team believes depth sensing is a useful and privacy-preserving "
                "approach for estimating food portions, but it may not identify every "
                "food or ingredient correctly. Mixed dishes, soups, sauces, and "
                "restaurant foods may be especially difficult. We suggest using "
                "depth sensing as the primary method while asking users to verify "
                "food information when necessary."
            ),
            (
                "Our team recommends funding the project as a pilot study with some "
                "reservations. Combining food recording, activity tracking, and "
                "personalized feedback in one wearable device is promising. However, "
                "the team must demonstrate measurement validity, usability, privacy, "
                "and confidentiality. A successful pilot would establish feasibility, "
                "but larger and longer studies would still be needed to evaluate "
                "long-term health effects."
            ),
        ],
    },
    {
        "name": "human versus AI score separation",
        "criterion": 2,
        # The first five are human-written; the final five are AI test samples.
        "split_after": 5,
        "texts": [
            (
                "Our team believes one or two personal reminders each day may help "
                "people develop healthy habits. The advice should be straightforward "
                "and match the person's preferences. Repetitive or inaccurate "
                "notifications may cause users to stop paying attention."
            ),
            (
                "Depth sensing is useful for privacy because it can measure volume "
                "without continuously storing color photographs. It still cannot "
                "identify every ingredient, so user confirmation remains important."
            ),
            (
                "The pilot study can show whether people are willing to wear the "
                "device and follow its recommendations. It cannot by itself prove "
                "that the device prevents cancer or produces lasting behavior change."
            ),
            (
                "Before supporting the proposal, we would require a clear strategy "
                "for comparing its measurements with established methods. We would "
                "also want direct feedback from participants about comfort and privacy."
            ),
            (
                "Thirty participants over twelve weeks is a reasonable beginning. "
                "The study should be treated as a feasibility test, followed by a "
                "larger study if the measurements and user experience are acceptable."
            ),
            (
                "The implementation of the proposed framework requires careful "
                "consideration of several important factors. First, the system must "
                "process information efficiently. Second, the system must provide "
                "consistent and reliable outputs. Finally, continuous evaluation is "
                "essential for ensuring optimal performance across diverse conditions."
            ),
            (
                "Effective communication is an essential component of organizational "
                "success. Teams that communicate clearly are better positioned to "
                "achieve objectives. Furthermore, structured collaboration enables "
                "stakeholders to exchange information efficiently and produce "
                "consistent outcomes."
            ),
            (
                "Artificial intelligence provides numerous opportunities to improve "
                "modern systems. It can increase efficiency, support decision-making, "
                "and automate repetitive tasks. Organizations should therefore adopt "
                "responsible strategies that maximize benefits while minimizing "
                "potential risks."
            ),
            (
                "Time management is important in today's fast-paced environment. "
                "Individuals should identify priorities, minimize distractions, and "
                "schedule regular breaks. These strategies can improve productivity, "
                "reduce stress, and support the successful completion of objectives."
            ),
            (
                "The proposed solution offers a comprehensive and scalable approach. "
                "By integrating advanced technologies with established best practices, "
                "the framework can enhance accuracy, reliability, and overall user "
                "satisfaction. Regular monitoring will support continued improvement."
            ),
        ],
    },
    {
        "name": "all three labels reachable",
        "criterion": 3,
        "expected_guesses": ["human", "unsure", "ai"],
        "texts": [
            (
                "According to research published by Stanford, careful evaluation of "
                "AI remains necessary. I reviewed the source while preparing my notes: "
                "https://hai.stanford.edu/"
            ),
            (
                "The system works well. It handles cases correctly and provides useful "
                "results. I tested it yesterday, but I am still uncertain whether its "
                "behavior will remain consistent on less ordinary examples."
            ),
            (
                "The implementation requires careful consideration of important "
                "factors. The system provides effective results. The framework supports "
                "consistent outcomes. The solution improves efficiency. The process "
                "ensures reliable performance. The method delivers valuable benefits."
            ),
        ],
    },
    {
        "name": "appeal changes status and is logged",
        "criterion": 4,
        "appeal": True,
        "texts": [
            "I wrote this paragraph while reviewing my class notes.",
            "This is my original explanation of the project requirements.",
            "I drafted this response and revised it before submitting it.",
            "These sentences describe my own understanding of the topic.",
            "I am requesting review because I wrote this submission myself.",
        ],
    },
    {
        "name": "invalid submissions rejected safely",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": 12345, "creator_id": "eval_bad_number"},
            {"text": "word " * 13000, "creator_id": "eval_bad_huge"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
