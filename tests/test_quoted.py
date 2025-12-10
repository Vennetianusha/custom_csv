# tests/test_quoted.py
import io
from parser import CSVParser

def test_quoted_commas_and_escapes():
    s = io.StringIO('a,"b,with,comma","c""quote""",d\n')
    rows = list(CSVParser().read_rows(s))
    assert rows == [['a', 'b,with,comma', 'c"quote"', 'd']]

def test_unquoted_and_spaces_preserved():
    s = io.StringIO('x, y ," z "\n')
    rows = list(CSVParser().read_rows(s))
    assert rows == [['x', ' y ', ' z ']]
