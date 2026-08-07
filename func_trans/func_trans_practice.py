from collections.abc import Callable

"""
Complete the get_filter_cmd function. It takes two functions as input, filter_one and filter_two, and returns a function, filter_cmd.

filter_cmd itself should take as input two strings: content and option.

1. Set the default value of the option argument to "--one".
2. Complete filter_cmd so that it filters and returns the content according to the input option.
    a. If "--one", use filter_one.
    b. If "--two", use filter_two.
    c. If "--three", use filter_one first, then filter_two.
    d. If any other option is passed, raise an exception:
       "invalid option"
"""


def get_filter_cmd(
    filter_one: Callable[[str], str], filter_two: Callable[[str], str]
) -> Callable[[str, str], str]:
    def filter_cmd(content: str, option: str = "--one") -> str:
        if option == "--one":
            return filter_one(content)
        elif option == "--two":
            return filter_two(content)
        elif option == "--three":
            return filter_two(filter_one(content))
        else:
            raise ValueError("invalid option")

    return filter_cmd


# Don't touch below this line


def replace_bad(text: str) -> str:
    return text.replace("bad", "good")


def replace_ellipsis(text: str) -> str:
    return text.replace("..", "...")


def fix_ellipsis(text: str) -> str:
    return text.replace("....", "...")
