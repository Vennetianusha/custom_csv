# parser.py
from typing import Iterator, List, TextIO

class CSVParser:
    def __init__(self, delimiter: str = ",", quotechar: str = '"', skip_blank_lines: bool = True):
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.skip_blank_lines = skip_blank_lines

    # ------------------------------------------------------------
    # FAST _parse_line (micro-optimized)
    # ------------------------------------------------------------
    def _parse_line(self, line: str) -> List[str]:
        """Fast parse of a single logical CSV line."""
        delim = self.delimiter
        dq = self.quotechar
        fields: List[str] = []
        cur: List[str] = []
        cur_append = cur.append
        i = 0
        n = len(line)
        in_quotes = False

        while i < n:
            ch = line[i]

            if in_quotes:
                if ch == dq:
                    # Escaped quote ("")
                    if i + 1 < n and line[i+1] == dq:
                        cur_append(dq)
                        i += 2
                        continue
                    else:
                        in_quotes = False
                        i += 1
                        continue
                else:
                    cur_append(ch)

            else:  # not in quotes
                if ch == dq:
                    in_quotes = True
                elif ch == delim:
                    fields.append("".join(cur))
                    cur = []
                    cur_append = cur.append
                else:
                    cur_append(ch)

            i += 1

        fields.append("".join(cur))
        return fields

    # ------------------------------------------------------------
    # read_rows (supports embedded newlines!)
    # ------------------------------------------------------------
    def read_rows(self, file_obj: TextIO) -> Iterator[List[str]]:
        buffer = ""

        for raw in file_obj:
            buffer += raw  # keep newline

            # Check if buffer has unmatched quote
            in_quotes = False
            i = 0
            while i < len(buffer):
                ch = buffer[i]
                if in_quotes:
                    if ch == self.quotechar:
                        # escaped?
                        if i + 1 < len(buffer) and buffer[i+1] == self.quotechar:
                            i += 2
                            continue
                        else:
                            in_quotes = False
                    i += 1
                else:
                    if ch == self.quotechar:
                        in_quotes = True
                    i += 1

            # If still in quotes → wait for next line
            if in_quotes:
                continue

            # Extract logical rows (split only newlines OUTSIDE quotes)
            logical_rows: List[str] = []
            start = 0
            in_quotes = False
            i = 0
            while i < len(buffer):
                ch = buffer[i]
                if in_quotes:
                    if ch == self.quotechar:
                        if i + 1 < len(buffer) and buffer[i+1] == self.quotechar:
                            i += 2
                            continue
                        else:
                            in_quotes = False
                            i += 1
                            continue
                    else:
                        i += 1
                        continue
                else:
                    if ch == self.quotechar:
                        in_quotes = True
                        i += 1
                        continue

                    if ch == "\n":
                        logical_rows.append(buffer[start:i])
                        start = i + 1

                    i += 1

            buffer = buffer[start:]

            # Yield parsed rows
            for lr in logical_rows:
                parsed = self._parse_line(lr)
                if self.skip_blank_lines and all(cell == "" for cell in parsed):
                    continue
                yield parsed

        # EOF
        if buffer:
            # Check for open quote before final row
            in_quotes = False
            i = 0
            while i < len(buffer):
                ch = buffer[i]
                if in_quotes:
                    if ch == self.quotechar:
                        if i + 1 < len(buffer) and buffer[i+1] == self.quotechar:
                            i += 2
                            continue
                        else:
                            in_quotes = False
                    i += 1
                else:
                    if ch == self.quotechar:
                        in_quotes = True
                    i += 1

            if in_quotes:
                raise ValueError("EOF reached while inside a quoted field")

            parsed = self._parse_line(buffer.rstrip("\n"))
            if self.skip_blank_lines and all(cell == "" for cell in parsed):
                return
            yield parsed

    def read_all(self, file_obj: TextIO) -> List[List[str]]:
        return list(self.read_rows(file_obj))
