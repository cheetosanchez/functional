from copy import deepcopy
from collections.abc import Callable

Styles = dict[str, dict[str, str]]

# Don't touch above this line


def css_styles(initial_styles: Styles) -> Callable[[str, str, str], Styles]:
    styles = deepcopy(initial_styles)

    def add_style(selector: str, property: str, value: str) -> Styles:
        if selector not in styles:
            styles[selector] = {}
        styles[selector][property] = value
        return styles

    return add_style
