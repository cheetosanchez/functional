from recursion_practice1 import find_longest_word

TestCase = tuple[str, str]

run_cases: list[TestCase] = [
    ("Either that wallpaper goes, or I do.", "wallpaper"),
    (
        "Then I die happy",
        "happy",
    ),
    (
        "Et tu, Brute?",
        "Brute?",
    ),
    (
        "Do not disturb my circles",
        "disturb",
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        "",
        "",
    ),
    (
        " ",
        "",
    ),
    (
        "Let us cross over the river and rest under the shade of the trees",
        "cross",
    ),
]


def test(document: str, expected: str) -> bool:
    print("---------------------------------")
    print(f"Input: '{document}'")
    print(f"Expected: '{expected}'")
    result = find_longest_word(document)
    print(f"Actual:   '{result}'")
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
