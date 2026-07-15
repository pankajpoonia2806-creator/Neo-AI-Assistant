import sqlite3


class Memory:

    def __init__(self):

        self.conn = sqlite3.connect(
            "database.db",
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        # ---------------- User Memory ---------------- #

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            memory_key TEXT,
            memory_value TEXT,
            source TEXT,
            importance INTEGER DEFAULT 5,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # ---------------- Chat History ---------------- #

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.conn.commit()

    # ---------------- Save Memory ---------------- #

    def save_memory(
        self,
        category,
        key,
        value,
        source="user",
        importance=5
    ):

        self.cursor.execute(
            """
            INSERT INTO memories
            (
                category,
                memory_key,
                memory_value,
                source,
                importance
            )
            VALUES(?,?,?,?,?)
            """,
            (
                category,
                key,
                value,
                source,
                importance
            )
        )

        self.conn.commit()

    # ---------------- Get Memory ---------------- #

    def get_memory(self, key):

        self.cursor.execute(
            """
            SELECT memory_value
            FROM memories
            WHERE memory_key=?
            ORDER BY id DESC
            LIMIT 1
            """,
            (key,)
        )

        row = self.cursor.fetchone()

        return row[0] if row else None

    # ---------------- All Memories ---------------- #

    def get_all_memories(self):

        self.cursor.execute("""
        SELECT
            category,
            memory_key,
            memory_value,
            importance
        FROM memories
        ORDER BY id DESC
        """)

        return self.cursor.fetchall()
        # ---------------- Search Memory ---------------- #

    def search_memory(self, keyword):

        self.cursor.execute(
            """
            SELECT
                category,
                memory_key,
                memory_value
            FROM memories
            WHERE
                memory_key LIKE ?
                OR memory_value LIKE ?
            ORDER BY id DESC
            """,
            (
                f"%{keyword}%",
                f"%{keyword}%"
            )
        )

        return self.cursor.fetchall()

    # ---------------- Delete Memory ---------------- #

    def delete_memory(self, key):

        self.cursor.execute(
            """
            DELETE FROM memories
            WHERE memory_key=?
            """,
            (key,)
        )

        self.conn.commit()

    # ---------------- Save Chat ---------------- #

    def save_chat(self, role, message):

        self.cursor.execute(
            """
            INSERT INTO chat_history
            (
                role,
                message
            )
            VALUES(?,?)
            """,
            (
                role,
                message
            )
        )

        self.conn.commit()

    # ---------------- Load Chat ---------------- #

    def load_chat(self, limit=30):

        self.cursor.execute(
            """
            SELECT
                role,
                message
            FROM chat_history
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        rows = self.cursor.fetchall()

        rows.reverse()

        history = []

        for role, message in rows:

            history.append(
                {
                    "role": role,
                    "content": message
                }
            )

        return history

    # ---------------- Clear Chat ---------------- #

    def clear_chat(self):

        self.cursor.execute(
            "DELETE FROM chat_history"
        )

        self.conn.commit()

    # ---------------- Close ---------------- #

    def close(self):

        self.conn.close()