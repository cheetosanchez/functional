def choose_parser(file_extension: str) -> str:
    # if file_extension.lower() in ("markdown", "md"):
    #     return "markdown"
    # else:
    #     return "plaintext"

    return "markdown" if file_extension.lower() in ("markdown", "md") else "plaintext"
