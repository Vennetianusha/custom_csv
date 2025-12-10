# tests/test_embedded_newline.py
import io
from parser import CSVParser

def test_embedded_newline_in_quoted_field():
    text = 'id,notes\n1,"line1\nline2\nline3",end\n2,ok,here\n'
    s = io.StringIO(text)
    rows = list(CSVParser().read_rows(s))
    assert rows[0] == ['id','notes']
    assert rows[1] == ['1', 'line1\nline2\nline3', 'end']
    assert rows[2] == ['2','ok','here']
