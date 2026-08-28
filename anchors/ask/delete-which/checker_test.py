import sqlite3
from app.migrate import apply_all
from app.users import display_name


def test_still_works():
    conn = sqlite3.connect(":memory:")
    apply_all(conn)
    conn.execute("INSERT INTO users (id, name, nickname) VALUES (1, 'Ada', 'ada')")
    assert display_name(conn, 1) == "ada"
