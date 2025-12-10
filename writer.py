# writer.py
from typing import Iterable, List, TextIO

class CSVWriter:
    def __init__(self, delimiter: str = ",", quotechar: str = '"'):
        self.delimiter = delimiter
        self.quotechar = quotechar

    def write_row(self, file_obj: TextIO, row: Iterable[str]) -> None:
        out_fields: List[str] = []
        for raw in row:
            s = str(raw)
            needs_quote = (self.delimiter in s) or (self.quotechar in s) or ("\n" in s)
            if needs_quote:
                # escape internal quotes by doubling, then wrap in quotes
                inner = s.replace(self.quotechar, self.quotechar * 2)
                out_fields.append(self.quotechar + inner + self.quotechar)
            else:
                out_fields.append(s)
        file_obj.write(self.delimiter.join(out_fields) + "\n")

    def write_rows(self, file_obj: TextIO, rows: Iterable[Iterable[str]]) -> None:
        for r in rows:
            self.write_row(file_obj, r)
