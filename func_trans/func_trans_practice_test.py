from collections.abc import Callable

import func_trans_practice as student

FilterFunc = Callable[[str], str]
FilterArgs = tuple[str, ...]
FilterCase = tuple[FilterArgs, str]
TestCase = tuple[str, FilterFunc, str, FilterFunc, list[FilterCase]]

run_cases: list[TestCase] = [
    (
        "replace_bad",
        student.replace_bad,
        "replace_ellipsis",
        student.replace_ellipsis,
        [
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                ),
                "I'm good, and that's good. I will never be good, and that's not good..",
            ),
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                    "--one",
                ),
                "I'm good, and that's good. I will never be good, and that's not good..",
            ),
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                    "--two",
                ),
                "I'm bad, and that's good. I will never be good, and that's not bad...",
            ),
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                    "--three",
                ),
                "I'm good, and that's good. I will never be good, and that's not good...",
            ),
        ],
    ),
]

submit_cases: list[TestCase] = [
    *run_cases,
    (
        "replace_ellipsis",
        student.replace_ellipsis,
        "fix_ellipsis",
        student.fix_ellipsis,
        [
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                ),
                "There's no place like home... but sometimes, it's nice to get away.... and explore......",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "--one",
                ),
                "There's no place like home... but sometimes, it's nice to get away.... and explore......",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "--two",
                ),
                "There's no place like home.. but sometimes, it's nice to get away... and explore...",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "--three",
                ),
                "There's no place like home... but sometimes, it's nice to get away... and explore.....",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "",
                ),
                "invalid option",
            ),
        ],
    ),
]


def test(
    filter_one_name: str,
    filter_one: FilterFunc,
    filter_two_name: str,
    filter_two: FilterFunc,
    test_cases: list[FilterCase],
) -> bool:
    print("---------------------------------")
    print(f"Input functions: {filter_one_name} and {filter_two_name}")
    filter_cmd = student.get_filter_cmd(filter_one, filter_two)
    failed = False
    for case in test_cases:
        print("Calling filter_cmd with:")
        print(f" * content: {case[0][0]}")
        if len(case[0]) > 1:
            print(f" * option: {case[0][1]}")
        else:
            print(" * option: (default)")
        try:
            result = filter_cmd(*case[0])
        except Exception as e:
            result = str(e)
        expected_output = case[1]
        print(f"Expected: {expected_output}")
        print(f"Actual:   {result}")
        if result != expected_output:
            failed = True
            print("Fail")
        else:
            print("Pass")
    passed = not failed
    return passed


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
