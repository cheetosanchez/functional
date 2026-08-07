def change_bullet_style(document: str) -> str:
    lines = document.split("\n")
    mapped = map(convert_line, lines)
    joined = "\n".join(mapped)
    return joined


# Don't edit below this line


def convert_line(line: str) -> str:
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
