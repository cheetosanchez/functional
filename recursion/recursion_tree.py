def list_files(
    parent_directory: dict[str, dict | None], current_filepath: str = ""
) -> list[str]:
    filepaths = []
    for node in parent_directory:
        next = parent_directory[node]
        if next is None:
            filepaths.append(f"{current_filepath}/{node}")
        else:
            next_filepaths = list_files(next, f"{current_filepath}/{node}")
            filepaths.extend(next_filepaths)
    return filepaths
