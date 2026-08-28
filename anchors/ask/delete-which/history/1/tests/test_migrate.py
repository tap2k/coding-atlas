import sqlite3

from app.migrate import apply_all
from app.users import display_name


def test_chain_applies():
    conn = sqlite3.connect(":memory:")
    assert apply_all(conn) == ["0001_initial", "0002_add_nickname"]


def test_display_name():
    conn = sqlite3.connect(":memory:")
    apply_all(conn)
    conn.execute("INSERT INTO users (id, name, nickname) VALUES (1, 'Ada', 'ada')")
    assert display_name(conn, 1) == "ada"
