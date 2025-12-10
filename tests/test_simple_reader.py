# tests/test_simple_reader.py
import io
from parser import CSVParser

def test_simple_split():
    s = io.StringIO("a,b,c\n1,2,3\n")
    rows = list(CSVParser().read_rows(s))
    assert rows == [["a","b","c"], ["1","2","3"]]

def test_trailing_newline_and_whitespace():
    s = io.StringIO("x, y ,z\n")
    rows = list(CSVParser().read_rows(s))
    assert rows == [["x"," y ","z"]]
