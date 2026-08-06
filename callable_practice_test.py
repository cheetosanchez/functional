from typing import Callable, get_type_hints

from callable_practice import apply_transform


def add_brackets(value: str) -> str:
    return "[" + value + "]"


def repeat(value: str) -> str:
    return value * 2


def add_status(value: str) -> str:
    return "Status: " + value


def first_character(value: str) -> str:
    if value == "":
        return ""
    return value[0]


run_cases = [
    (["online", "away"], add_brackets, "add_brackets", ["[online]", "[away]"]),
    (["go", "hi", "ok"], repeat, "repeat", ["gogo", "hihi", "okok"]),
]

submit_cases = run_cases + [
    ([], add_status, "add_status", []),
    (["", "alpha", "beta"], first_character, "first_character", ["", "a", "b"]),
    (
        ["ready", "waiting", "done"],
        add_status,
        "add_status",
        ["Status: ready", "Status: waiting", "Status: done"],
    ),
]


def test(strings, transform, transform_name, expected):
    print("---------------------------------")
    print(f"Input strings: {strings}")
    print(f"Transformation: {transform_name}")
    print("")

    try:
        hints = get_type_hints(apply_transform)
        expected_hints = {
            "strings": list[str],
            "transform": Callable[[str], str],
            "return": list[str],
        }
        print(f"Expected type hints: {expected_hints}")
        print(f"Actual type hints:   {hints}")
        if hints != expected_hints:
            print("Fail")
            return False

        result = apply_transform(strings, transform)
        print(f"Expected result: {expected}")
        print(f"Actual result:   {result}")
        if result == expected:
            print("Pass")
            return True
    except Exception as error:
        print(f"Error: {error}")

    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for test_case in test_cases:
        if test(*test_case):
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


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
