import sqlite3

conn = sqlite3.connect("memory.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memory(
id INTEGER PRIMARY KEY AUTOINCREMENT,
question TEXT,
answer TEXT
)
""")

conn.commit()

def save_chat(question, answer):
    cursor.execute(
        "INSERT INTO memory(question,answer) VALUES(?,?)",
        (question, answer)
    )
    conn.commit()

def load_history():
    cursor.execute("SELECT question,answer FROM memory")
    return cursor.fetchall()