import sqlite3

DB_NAME = "leaderboard.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        score INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_score(name, score):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, score))

    conn.commit()
    conn.close()


def get_leaderboard():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT name, score FROM scores ORDER BY score DESC")

    results = cursor.fetchall()

    conn.close()

    return results
