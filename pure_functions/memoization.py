def word_count_memo(document: str, memos: dict[str, int]) -> tuple[int, dict[str, int]]:
    new_memos = memos.copy()
    if document in new_memos:
        return new_memos[document], new_memos
    count = word_count(document)
    new_memos[document] = count
    return count, new_memos


# Don't edit below this line


def word_count(document: str) -> int:
    count = len(document.split())
    return count
