def add_format(default_formats: dict[str, bool], new_format: str) -> dict[str, bool]:
    default_formats[new_format] = True
    return default_formats


def remove_format(default_formats: dict[str, bool], old_format: str) -> dict[str, bool]:
    default_formats[old_format] = False
    return default_formats
