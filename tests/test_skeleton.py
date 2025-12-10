# tests/test_skeleton.py
import io
from parser import CSVParser
from writer import CSVWriter

def test_parser_has_read_rows_and_smoke():
    p = CSVParser()
    assert hasattr(p, "read_rows")
    # smoke test: simple input should be parsed by our simple reader
    assert list(p.read_rows(io.StringIO("a,b,c\n"))) == [["a","b","c"]]

def test_writer_has_write_row_and_smoke():
    w = CSVWriter()
    assert hasattr(w, "write_row")
    out = io.StringIO()
    w.write_row(out, ["a","b","c"])
    assert out.getvalue() == "a,b,c\n"
