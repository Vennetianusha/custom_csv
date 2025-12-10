# tests/test_edgecases.py
import io
import pytest
from parser import CSVParser

def test_blank_lines_skipped_by_default():
    text = "\nname,age\n\nAlice,30\n\n"
    s = io.StringIO(text)
    rows = list(CSVParser().read_rows(s))
    assert rows == [['name','age'], ['Alice','30']]

def test_blank_lines_can_be_included():
    text = "\n\n"
    s = io.StringIO(text)
    rows = list(CSVParser(skip_blank_lines=False).read_rows(s))
    assert rows == [[''], ['']]

def test_trailing_delimiter_produces_empty_field():
    s = io.StringIO("a,b,\n")
    rows = list(CSVParser().read_rows(s))
    assert rows == [['a','b','']]

def test_inconsistent_columns_are_parsed_not_normalized():
    text = "a,b,c\n1,2\n3,4,5,6\n"
    s = io.StringIO(text)
    rows = list(CSVParser().read_rows(s))
    # parser doesn't enforce fixed column count; it returns each row as parsed
    assert rows == [['a','b','c'], ['1','2'], ['3','4','5','6']]
