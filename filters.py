def remove_invalid_lines(document: str) -> str:
    filtered = filter(lambda line: not line.startswith("-"), document.split("\n"))
    return "\n".join(filtered)
