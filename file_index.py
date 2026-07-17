import sqlite3


class FileIndex:

    def __init__(self):

        self.create_table()

    def connect(self):

        return sqlite3.connect("files.db")

    def create_table(self):

        db = self.connect()
        cursor = db.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS files(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            path TEXT UNIQUE NOT NULL
        )
        """)

        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_name
        ON files(name)
        """)

        db.commit()
        db.close()

    def clear(self):

        db = self.connect()
        cursor = db.cursor()

        cursor.execute("DELETE FROM files")

        db.commit()
        db.close()

    def add(self, name, path):

        db = self.connect()
        cursor = db.cursor()

        cursor.execute(
            """
            INSERT OR IGNORE INTO files(name, path)
            VALUES (?, ?)
            """,
            (name.lower(), path)
        )

        db.commit()
        db.close()

    def save(self):
        # Commit is already done in add()
        pass

    def search(self, query):

        db = self.connect()
        cursor = db.cursor()

        cursor.execute(
            """
            SELECT name, path
            FROM files
            WHERE name LIKE ?
            LIMIT 10
            """,
            (f"%{query.lower()}%",)
        )

        results = cursor.fetchall()

        db.close()

        return results