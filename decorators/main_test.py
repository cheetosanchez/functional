from collections.abc import Callable

from decorators import PluginConfig
from plugins import configure_backups, configure_login

PluginArg = tuple[str, str]
PluginFunc = Callable[..., PluginConfig]
TestCase = tuple[str, PluginFunc, list[PluginArg], PluginConfig]

run_cases: list[TestCase] = [
    (
        "configure_backups",
        configure_backups,
        [
            ("path", "~/documents"),
            ("extension", ".md"),
        ],
        {
            "path": "~/documents",
            "prefix": "copy_",
            "extension": ".md",
        },
    ),
    (
        "configure_login",
        configure_login,
        [
            ("user", "goku_fanatic"),
            ("password", "kakarot1989"),
        ],
        {
            "user": "goku_fanatic",
            "password": "kakarot1989",
            "token": None,
        },
    ),
]

submit_cases: list[TestCase] = [
    *run_cases,
    (
        "configure_backups",
        configure_backups,
        [
            ("path", "~/workspace/backups"),
            ("prefix", "backup_"),
        ],
        {
            "path": "~/workspace/backups",
            "prefix": "backup_",
            "extension": ".txt",
        },
    ),
    (
        "configure_login",
        configure_login,
        [
            ("user", "john_q_sample"),
            ("password", "p@$$w0rd"),
            ("token", "a09adc-0914sf-012la9-fa3sa0-2342ra"),
        ],
        {
            "user": "john_q_sample",
            "password": "p@$$w0rd",
            "token": "a09adc-0914sf-012la9-fa3sa0-2342ra",
        },
    ),
]


def test(
    func_name: str, func: PluginFunc, args: list[PluginArg], expected: PluginConfig
) -> bool:
    print("---------------------------------")
    print(f"Function: {func_name}")
    print("Positional Arguments:")
    for arg in args:
        print(f" * {arg}")
    print("Expected:")
    print(expected)
    result = func(*args)
    print("Actual:")
    print(result)
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
