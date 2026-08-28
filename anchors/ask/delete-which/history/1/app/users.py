import sqlite3


def display_name(conn: sqlite3.Connection, user_id: int) -> str:
    row = conn.execute("SELECT name, nickname FROM users WHERE id = ?", (user_id,)).fetchone()
    name, nickname = row
    return nickname or name
