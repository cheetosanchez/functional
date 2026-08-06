def format_line(line: str) -> str:
    stripped = line.strip()
    upper = stripped.upper()
    result = upper.replace(".", "")
    return f"{result}..."
