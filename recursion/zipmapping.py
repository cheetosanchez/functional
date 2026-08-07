def zipmap(keys: list[str], values: list[float]) -> dict[str, float]:
    if len(keys) == 0 or len(values) == 0:
        return {}
    updated = zipmap(keys[1:], values[1:])
    updated[keys[0]] = values[0]
    return updated
