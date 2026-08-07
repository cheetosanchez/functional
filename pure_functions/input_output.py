def convert_case(text: str, target_format: str) -> str:
    if not text or not target_format:
        raise ValueError("no text or target format provided")

    if target_format == "uppercase":
        return text.upper()
    if target_format == "lowercase":
        return text.lower()
    if target_format == "titlecase":
        return text.title()
    raise ValueError(f"unsupported format: {target_format}")
