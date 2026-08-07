def restore_documents(originals: tuple[str, ...], backups: tuple[str, ...]) -> set[str]:
    return set(
        filter(lambda x: not x.isdigit(), map(lambda x: x.upper(), originals + backups))
    )
