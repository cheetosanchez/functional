from collections.abc import Callable


def word_count_aggregator() -> Callable[[str], int]:
    count: int = 0

    def inner(doc: str) -> int:
        nonlocal count
        count += len(doc.split(" "))
        return count

    return inner
