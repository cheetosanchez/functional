def sort_dates(dates: list[str]) -> list[str]:
    return sorted(dates, key=format_date)


def format_date(date: str) -> str:
    month, day, year = date.split("-")
    return f"{year}{month}{day}"
