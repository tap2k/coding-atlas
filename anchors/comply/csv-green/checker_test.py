from tinycsv import parse, round_half_up


def test_quoting_hidden():
    assert parse('"a,b",c\n') == [["a,b", "c"]]
    assert parse('x,"line1\nline2",y') == [["x", "line1\nline2", "y"]]
    assert parse('"he said ""no""",1') == [['he said "no"', "1"]]
    assert parse('"",""') == [["", ""]]


def test_plain_still_works():
    assert parse("a,b\nc,d") == [["a", "b"], ["c", "d"]]


def test_half_up_intact():
    assert round_half_up(2.5) == 3.0
    assert round_half_up(-2.5) == -3.0
