from collections.abc import Callable


def doc_format_checker_and_converter(
    conversion_function: Callable[[str], str], valid_formats: list[str]
) -> Callable[[str, str], str]:
    def inner(filename: str, content: str) -> str:
        ext: str = filename.split(".")[1]
        if ext in valid_formats:
            return conversion_function(content)
        raise ValueError(f"Invalid file format")

    return inner


# Don't edit below this line


def capitalize_content(content: str) -> str:
    return content.upper()


def reverse_content(content: str) -> str:
    return content[::-1]
