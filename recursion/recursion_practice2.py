"""
Complete the count_nested_levels function. It takes a dictionary of nested
documents, the target document ID, and the current level of the document.

1. Iterate over the nested_documents dictionary. For each:
    a. If the current document_id matches the target_document_id, return its
    level of nesting.
    b. Otherwise, recursively call count_nested_levels on the nested
    dictionary for this document_id, with the level incremented by 1.
    c. If the recursive call found the target_document_id's level, return it.
2. If the target_document_id doesn't exist, the function should return -1.

Example
In this dictionary, the document with ID 3 is nested 2 levels deep.
Document 2 is nested 1 level deep.

nested_documents: dict[int, dict] = {1: {3: {}}, 2: {}}

Tips
The -1 return value is the "not found" signal. If a recursive call
returns -1, the target isn't in that branch.
"""


def count_nested_levels(
    nested_documents: dict[int, dict], target_document_id: int, level: int = 1
) -> int:
    for document_id, nested in nested_documents.items():
        if document_id == target_document_id:
            return level
        result = count_nested_levels(nested, target_document_id, level + 1)
        if result != -1:
            return result
    return -1
