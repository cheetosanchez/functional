def get_median_font_size(font_sizes: list[int]) -> int | None:
    if len(font_sizes) == 0:
        return None
    return sorted(font_sizes)[(len(font_sizes) - 1) // 2]
