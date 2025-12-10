# tests/test_writer.py
import io
from writer import CSVWriter

def test_writer_quotes_needed():
    out = io.StringIO()
    CSVWriter().write_row(out, ['a','b,1','c"hi"'])
    # internal quotes become doubled, then the whole field is wrapped in quotes
    assert out.getvalue() == 'a,"b,1","c""hi"""\n'

def test_writer_no_quotes_simple():
    out = io.StringIO()
    CSVWriter().write_row(out, ['x','y','z'])
    assert out.getvalue() == 'x,y,z\n'
