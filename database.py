import sqlite3
import threading

class VideoDatabase:
    def __init__(self, db_name="videos.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()
        self.migrate_schema()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS videos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    path TEXT NOT NULL,
                    title TEXT,
                    duration TEXT,
                    resolution TEXT,
                    thumbnail TEXT
                )
            """)

    def migrate_schema(self):
        try:
            with self.connection:
                self.connection.execute("ALTER TABLE videos ADD COLUMN thumbnail TEXT")
        except sqlite3.OperationalError:
            # This error occurs if the column already exists, which is fine
            pass

    def add_video(self, path, title, duration, resolution, thumbnail):
        with self.connection:
            self.connection.execute("""
                INSERT INTO videos (path, title, duration, resolution, thumbnail)
                VALUES (?, ?, ?, ?, ?)
            """, (path, title, duration, resolution, thumbnail))

    def get_all_videos(self):
        with self.connection:
            return self.connection.execute("SELECT * FROM videos").fetchall()


    def close(self):
        self.connection.close()
