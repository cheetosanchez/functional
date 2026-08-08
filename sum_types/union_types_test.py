from union_types import Parsed, ParseError, display_parse_result, parse_document

ExpectedType = type[Parsed] | type[ParseError]
TestCase = tuple[str, str, ExpectedType, str]

run_cases: list[TestCase] = [
    (
        "why_fp.txt",
        "Because functions are easier to test",
        Parsed,
        "Parsed why_fp.txt: 36 characters",
    ),
    ("why_fp.md", "", ParseError, "Failed why_fp.md: no content"),
]

submit_cases: list[TestCase] = run_cases + [
    (
        "functional-patterns.txt",
        "Unions make alternative states explicit",
        Parsed,
        "Parsed functional-patterns.txt: 39 characters",
    ),
    ("empty.md", "", ParseError, "Failed empty.md: no content"),
]


def test(
    doc_name: str, content: str, expected_type: ExpectedType, expected_msg: str
) -> bool:
    print("---------------------------------")
    print(f"Parsing document: {doc_name}")
    print(f"Content length: {len(content)}")
    result = parse_document(doc_name, content)
    actual_type = type(result)
    print(f"Expected type: {expected_type.__name__}")
    print(f"Actual type: {actual_type.__name__}")
    if actual_type is not expected_type:
        print("Fail")
        return False
    if result.doc_name != doc_name:
        print(f"Expected doc_name: {doc_name}")
        print(f"Actual doc_name: {result.doc_name}")
        print("Fail")
        return False
    if isinstance(result, Parsed):
        if result.text != content:
            print(f"Expected text: {content}")
            print(f"Actual text: {result.text}")
            print("Fail")
            return False
    if isinstance(result, ParseError):
        if result.err != "no content":
            print('Expected err: "no content"')
            print(f"Actual err: {result.err}")
            print("Fail")
            return False
    actual_msg = display_parse_result(result)
    print(f"Expected message: {expected_msg}")
    print(f"Actual message: {actual_msg}")
    if actual_msg != expected_msg:
        print("Fail")
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
