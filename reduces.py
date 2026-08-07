from functools import reduce


def join(doc_so_far: str, sentence: str) -> str:
    return f"{doc_so_far}. {sentence}"


def join_first_sentences(sentences: list[str], n: int) -> str:
    if n == 0:
        return ""
    return reduce(join, sentences[:n]) + "."
