# nickname moved to profile; users.nickname to be dropped once callers are migrated
def up(conn):
    conn.execute("CREATE TABLE profile (user_id INTEGER PRIMARY KEY, nickname TEXT, bio TEXT)")
