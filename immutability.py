def add_prefix(document: str, documents: tuple[str, ...]) -> tuple[str, ...]:
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    documents += (new_doc,)
    return documents
