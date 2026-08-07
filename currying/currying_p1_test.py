from currying_p1 import lines_with_sequence

TestCase = tuple[str, int, str, int]

run_cases: list[TestCase] = [
    (
        "#",
        3,
        """###
@##
$$$
###""",
        2,
    ),
    (
        "$",
        2,
        """$$$
$
***
@@@
$$
$$$""",
        3,
    ),
]

submit_cases: list[TestCase] = run_cases + [
    ("%", 1, "", 0),
    (
        "*",
        3,
        """***
*
$$$$$$
xxx
****
***
***""",
        4,
    ),
    (
        " ",
        1,
        """a a
bbb
 c""",
        2,
    ),
]


def test(char: str, length: int, doc: str, expected: int) -> bool:
    print("---------------------------------")
    print(f"Input char: {char}")
    print(f"Input length: {length}")
    print("Input doc:")
    print(doc)
    print(f"Expected: {expected}")
    num_lines = lines_with_sequence(char)(length)(doc)
    print(f"Actual:   {num_lines}")
    if num_lines == expected:
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
