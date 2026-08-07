from closures_practice1 import new_collection

TestCase = tuple[list[str], list[str], list[str]]

run_cases: list[TestCase] = [
    (["Dan Evans"], ["Charlie Prince"], ["Dan Evans", "Charlie Prince"]),
    (
        ["Dan Evans", "Ben Wade"],
        ["Alice Evans"],
        ["Dan Evans", "Ben Wade", "Alice Evans"],
    ),
    (
        ["Dan Evans", "Ben Wade", "Alice Evans"],
        ["Doc Potter", "Butterfield"],
        ["Dan Evans", "Ben Wade", "Alice Evans", "Doc Potter", "Butterfield"],
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        ["Dan Evans", "Ben Wade", "Alice Evans"],
        [],
        ["Dan Evans", "Ben Wade", "Alice Evans"],
    ),
    ([], ["William Evans"], ["William Evans"]),
    (
        ["Dan Evans", "Ben Wade"],
        ["Charlie Prince", "Butterfield"],
        ["Dan Evans", "Ben Wade", "Charlie Prince", "Butterfield"],
    ),
]


def test(initial_docs: list[str], new_docs: list[str], expected: list[str]) -> bool:
    print("---------------------------------")
    print(f"Initial documents: {initial_docs}")
    print(f"Documents to add: {new_docs}")
    print(f"Expected: {expected}")
    copy_of_initial_docs = initial_docs.copy()
    add_doc = new_collection(initial_docs)
    result: list[str] = initial_docs.copy()
    for doc in new_docs:
        result = add_doc(doc)
    print(f"Actual:   {result}")
    if copy_of_initial_docs != initial_docs:
        print("Fail: You should not modify the initial list")
        return False
    if result != expected:
        print("Fail: Unexpected result")
        return False
    print("Pass")
    return True


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
