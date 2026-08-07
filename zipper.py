valid_formats: list[str] = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(
    doc_names: list[str], doc_formats: list[str]
) -> list[tuple[str, str]]:
    zipped = zip(doc_names, doc_formats)
    filtered = filter(lambda x: x[1] in valid_formats, zipped)
    return list(filtered)
