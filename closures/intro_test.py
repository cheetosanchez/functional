from intro import word_count_aggregator

TestCase = tuple[list[str], int]

run_cases: list[TestCase] = [
    (
        [
            "Welcome to the jungle",
            "We've got fun and games",
            "We've got everything you want honey",
        ],
        15,
    )
]

submit_cases: list[TestCase] = run_cases + [
    (
        [
            "We are the champions my friends",
            "And we'll keep on fighting till the end",
        ],
        14,
    ),
    (
        [
            "I've got another confession to make",
            "I'm your fool",
            "Everyone's got their chains to break",
            "Holdin' you",
        ],
        17,
    ),
]


def test(input_docs: list[str], expected: int) -> bool:
    print("---------------------------------")
    print("Input:")
    for doc in input_docs:
        print(f" * {doc}")
    print(f"Expected: {expected}")

    aggregator = word_count_aggregator()

    result: int | Exception = AssertionError("No input docs")
    try:
        for input_doc in input_docs:
            result = aggregator(input_doc)
    except Exception as e:
        result = e

    print(f"Actual:   {result}")

    if result == expected:
        print("Pass")
        return True

    print("Fail")
    return False


def main() -> None:
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases: list[TestCase] = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
