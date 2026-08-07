doc: str = """I *love* Markdown.
I **really love** Markdown.
I ***really really love*** Markdown."""


def remove_emphasis(doc: str) -> str:
    lines = doc.split("\n")
    new_lines = map(remove_line_emphasis, lines)
    return "\n".join(new_lines)


# Don't touch below this line


def remove_line_emphasis(line: str) -> str:
    words = line.split()
    new_words = map(remove_word_emphasis, words)
    return " ".join(new_words)


def remove_word_emphasis(word: str) -> str:
    return word.strip("*")
