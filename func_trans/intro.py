from collections.abc import Callable


def get_logger(formatter: Callable[[str, str], str]) -> Callable[[str, str], None]:
    pass


# Don't edit below this line


def test(first: str, errors: list[str], formatter: Callable[[str, str], str]) -> None:
    print("Logs:")
    logger = get_logger(formatter)
    for err in errors:
        logger(first, err)
    print("====================================")


def colon_delimit(first: str, second: str) -> str:
    return f"{first}: {second}"


def dash_delimit(first: str, second: str) -> str:
    return f"{first} - {second}"


def main() -> None:
    db_errors: list[str] = [
        "out of memory",
        "cpu is pegged",
        "networking issue",
        "invalid syntax",
    ]
    test("Doc2Doc FATAL", db_errors, colon_delimit)

    mail_errors: list[str] = [
        "email too large",
        "non alphanumeric symbols found",
    ]
    test("Doc2Doc WARNING", mail_errors, dash_delimit)


main()
