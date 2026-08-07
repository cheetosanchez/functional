from collections.abc import Callable


def lines_with_sequence(char: str) -> Callable[[int], Callable[[str], int]]:
    def with_char(length: int) -> Callable[[str], int]:
        sequence = char * length

        def with_length(doc: str) -> int:
            lines: list[str] = doc.splitlines("\n")
            count: int = 0
            for line in lines:
                if sequence in line:
                    count += 1
            return count

        return with_length

    return with_char
