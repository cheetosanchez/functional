"""
Complete the get_csv_status function. It should use a match statement to
select the correct response depending on the status of the export operation.
Create functions to handle each operation as follows:

1. PENDING: return a tuple with the string "Pending..." and the raw table
data converted from a list of lists of anything, to a prepared list of
lists of strings.
    a. Try to use nested map functions to convert the data items into strings.
    b. Remember to convert from a map object back into a list.
2. PROCESSING: return a tuple with the string "Processing..." and the
prepared list of lists of strings converted to one CSV-formatted string.
    a. For each list of strings, combine the strings with join with commas
    in between to form a row.
    b. For each row string, combine the strings with join with
    newlines ("\n") in between to form a table.
3. SUCCESS: return a tuple with the string "Success!" and the data as-is.
4. FAILURE: return a tuple with the string "Unknown error, retrying..."
and the data after it's been prepared and processed into a CSV string,
by combining the steps for PENDING and PROCESSING.
5. For any other status, raise an Exception:
unknown export status

Tip
It's better if you try this challenge without using loops for practice,
but you may use loops.
"""

from enum import Enum
from typing import Any


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


RawCSVData = list[list[object]]
PreparedCSVData = list[list[str]]
CSVStatusResult = tuple[str, PreparedCSVData | str]

# Don't touch above this line


def get_csv_status(status: CSVExportStatus, data: Any) -> CSVStatusResult:
    match status:
        case CSVExportStatus.PENDING:
            prepared_data = list(map(lambda row: list(map(str, row)), data))
            return "Pending...", prepared_data
        case CSVExportStatus.PROCESSING:
            prepared_data = list(map(lambda row: list(map(str, row)), data))
            csv_string = "\n".join([",".join(row) for row in prepared_data])
            return "Processing...", csv_string
        case CSVExportStatus.SUCCESS:
            return "Success!", data
        case CSVExportStatus.FAILURE:
            prepared_data = list(map(lambda row: list(map(str, row)), data))
            csv_string = "\n".join([",".join(row) for row in prepared_data])
            return "Unknown error, retrying...", csv_string
        case _:
            raise Exception("unknown export status")
