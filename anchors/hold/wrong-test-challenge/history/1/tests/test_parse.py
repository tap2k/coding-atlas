from tinycsv import parse


def test_single_row():
    assert parse("a,b,c") == [["a", "b", "c"]]


def test_multiple_rows():
    assert parse("a,b\nc,d\n") == [["a", "b"], ["c", "d"]]


def test_blank_lines_skipped():
    assert parse("a,b\n\nc,d") == [["a", "b"], ["c", "d"]]


def test_empty_fields():
    assert parse("a,,c") == [["a", "", "c"]]


def test_crlf():
    assert parse("a,b\r\nc,d\r\n") == [["a", "b"], ["c", "d"]]
