def args_logger(*args: object, **kwargs: object) -> None:
    for i, arg in enumerate(args):
        print(f"{i + 1}. {arg}")
    for key, value in sorted(kwargs.items()):
        print(f"* {key}: {value}")
