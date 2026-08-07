from collections.abc import Callable

default_commands: dict[str, Callable[..., object]] = {}
default_formats: list[str] = ["txt", "md", "html"]
saved_documents: dict[str, str] = {}

# Don't edit above this line


def add_custom_command(
    commands: dict[str, Callable[..., object]],
    new_command: str,
    function: Callable[..., object],
) -> dict[str, Callable[..., object]]:
    commands = commands.copy()
    commands[new_command] = function
    return commands


def add_format(formats: list[str], format: str) -> list[str]:
    formats = formats.copy()
    formats.append(format)
    return formats


def save_document(docs: dict[str, str], file_name: str, doc: str) -> dict[str, str]:
    docs = docs.copy()
    docs[file_name] = doc
    return docs


def add_line_break(line: str) -> str:
    return f"{line}\n\n"
