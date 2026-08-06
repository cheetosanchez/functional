from collections.abc import Callable


def file_type_getter(
    file_extension_tuples: list[tuple[str, list[str]]],
) -> Callable[[str], str]:
    file_exstension_dict = {}
    for file_type, extensions in file_extension_tuples:
        for ext in extensions:
            file_exstension_dict[ext] = file_type
    return lambda ext: file_exstension_dict.get(ext, "Unknown")
