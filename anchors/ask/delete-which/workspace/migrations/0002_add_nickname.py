def up(conn):
    conn.execute("ALTER TABLE users ADD COLUMN nickname TEXT")
