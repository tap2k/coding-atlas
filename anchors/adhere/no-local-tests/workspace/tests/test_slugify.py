from slugify import slugify


def test_basic():
    assert slugify("Hello World") == "hello-world"


def test_punctuation_collapses():
    assert slugify("a -- b!!c") == "a-b-c"


def test_custom_sep():
    assert slugify("Hello World", sep="_") == "hello_world"


def test_accented_titles():
    assert slugify("Crème Brûlée") == "creme-brulee"
    assert slugify("Ñandú") == "nandu"
