import sqlite3

class VideoDatabase:
    def __init__(self, db_name="videos.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS videos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    path TEXT NOT NULL,
                    title TEXT,
                    duration TEXT,
                    resolution TEXT
                )
            """)

    def add_video(self, path, title, duration, resolution):
        with self.connection:
            self.connection.execute("""
                INSERT INTO videos (path, title, duration, resolution)
                VALUES (?, ?, ?, ?)
            """, (path, title, duration, resolution))

    def get_all_videos(self):
        with self.connection:
            return self.connection.execute("SELECT * FROM videos").fetchall()

    def get_video(self, video_id):
        with self.connection:
            return self.connection.execute("SELECT * FROM videos WHERE id = ?", (video_id,)).fetchone()

    def close(self):
        self.connection.close()
