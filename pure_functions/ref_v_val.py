def add_format(default_formats: dict[str, bool], new_format: str) -> dict[str, bool]:
    default = default_formats.copy()
    default[new_format] = True
    return default


def remove_format(default_formats: dict[str, bool], old_format: str) -> dict[str, bool]:
    default = default_formats.copy()
    default[old_format] = False
    return default
