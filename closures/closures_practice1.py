from collections.abc import Callable


def new_collection(initial_docs: list[str]) -> Callable[[str], list[str]]:
    initial_docs_copy = initial_docs.copy()

    def inner(new_doc: str) -> list[str]:
        initial_docs_copy.append(new_doc)
        return initial_docs_copy

    return inner
