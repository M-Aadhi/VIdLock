# video_manager.py
from PIL import Image, ImageTk
import cv2
import os
from database import VideoDatabase

class VideoManager:
    def __init__(self):
        self.video_db = VideoDatabase()   # Dictionary to store video passwords

    def extract_thumbnail(self, video_path):
        capture = cv2.VideoCapture(video_path)
        success, frame = capture.read()
        capture.release()
        if success:
            thumbnail_path = video_path + "_thumbnail.jpg"
            cv2.imwrite(thumbnail_path, frame)
            return thumbnail_path
        return None
    
    def add_video(self, video_path, metadata):
        thumbnail_path = self.extract_thumbnail(video_path)
        title = os.path.basename(video_path)
        duration = metadata.get('duration', '')
        resolution = metadata.get('resolution', '')
        self.video_db.add_video(video_path, title, duration, resolution, thumbnail_path)

    

    def list_videos(self):
        return self.video_db.get_all_videos()
    
    def get_video_metadata(self, video_path):
        """Get metadata for a specific video."""
        return 

    def mark_as_favorite(self, video_path,metadata):
        """Mark a video as favorite."""
        self.favorites[video_path] = metadata

    def list_favorites(self):
        """List all favorite videos."""
        return list(self.favorites.keys())

    def add_personal_video(self, video_path, metadata, password):
        """Add a personal video with password protection."""
        self.personal[video_path] = {"metadata": metadata, "password": password}

    def unlock_personal_video(self, video_path, password):
        """Unlock a personal video with the correct password."""
        if video_path in self.personal:
            if password == self.personal[video_path]["password"]:
                return True
        return False
