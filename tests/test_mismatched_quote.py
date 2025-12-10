# tests/test_mismatched_quote.py
import io
import pytest
from parser import CSVParser

def test_mismatched_quote_raises():
    s = io.StringIO('a,"b,c\n')  # missing closing quote and EOF
    with pytest.raises(ValueError):
        list(CSVParser().read_rows(s))
