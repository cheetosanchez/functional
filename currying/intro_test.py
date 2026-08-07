from intro import converted_font_size

TestCase = tuple[int, str, int | str]

run_cases: list[TestCase] = [
    (12, "txt", 12),
    (16, "md", 32),
]

submit_cases: list[TestCase] = run_cases + [
    (14, "html", "invalid doc type"),
    (0, "txt", 0),
    (50, "md", 100),
]


def test(font_size: int, doc_type: str, expected: int | str) -> bool:
    print("---------------------------------")
    print("Inputs:")
    print(f" * font_size: {font_size}")
    print(f" * doc_type: {doc_type}")
    print(f"Expected: {expected}")
    try:
        result = converted_font_size(font_size)(doc_type)
    except Exception as error:
        result = str(error)
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
