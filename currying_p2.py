from collections.abc import Callable

"""
Complete the create_markdown_image function using currying. It takes 
a string input, alt_text.

1. Enclose the alt_text in square brackets prefixed with an 
exclamation point: ![alt_text]
2. Define an inner function that also takes a string input, url:
    a. The inner function should first escape any parentheses in the URL by replacing them with encoded sequences.
        i. Use the .replace() string method to change any opening 
        parenthesis ( into %28.
        ii. Do the same to change any closing parenthesis ) into %29.
    b. Enclose the url with parentheses: (url)
    c. Add the enclosed url to the end of the enclosed 
    alt_text: ![alt_text](url)
    d. Define the innermost function. It should take an optional string input for the title (title=None).
        i. If a title is passed:
            - Enclose it in double quotes.
            - Add the quoted title to the image syntax by first removing 
            the closing parenthesis ) from the end of the image syntax.
            - Add a space and the quoted title with a closing parenthesis ) 
            to the end of the image syntax: ![alt_text](url "title")
        ii. Return the finished image syntax.
    e. Return the innermost function.
3. Return the inner function.
"""


def create_markdown_image(alt_text: str) -> Callable[[str], Callable[..., str]]:
    # 1. Enclose the alt_text in square brackets prefixed with an exclamation point: ![alt_text]
    image_syntax = f"![{alt_text}]"
