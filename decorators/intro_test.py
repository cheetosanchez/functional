from intro import process_doc

Inputs = tuple[str, str]
Output = tuple[str, dict[str, int]]
TestCase = tuple[Inputs, Output]

run_cases: list[TestCase] = [
    (
        ("Welcome to the jungle", "txt"),
        ("Processing doc: 'Welcome to the jungle'. File Type: txt", {"txt": 1}),
    ),
    (
        ("We've got fun and games", "txt"),
        ("Processing doc: 'We've got fun and games'. File Type: txt", {"txt": 2}),
    ),
    (
        ("We've got *everything* you want honey", "md"),
        (
            "Processing doc: 'We've got *everything* you want honey'. File Type: md",
            {"txt": 2, "md": 1},
        ),
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        ("We are the champions my friends", "docx"),
        (
            "Processing doc: 'We are the champions my friends'. File Type: docx",
            {"txt": 2, "md": 1, "docx": 1},
        ),
    ),
    (
        ("print('hello world')", "py"),
        (
            "Processing doc: 'print('hello world')'. File Type: py",
            {"txt": 2, "md": 1, "docx": 1, "py": 1},
        ),
    ),
]


def test(inputs: Inputs, expected: Output) -> bool:
    print("---------------------------------")
    print("Inputs:")
    for inp in inputs:
        print(f" * {inp}")
    print("Expected:")
    for out in expected:
        print(f" * {out}")
    counts: Output = process_doc(*inputs)
    print("Actual:")
    for out in counts:
        print(f" * {out}")

    if counts == expected:
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
