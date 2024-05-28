# video_manager.py

class VideoManager:
    def __init__(self):
        self.library = {}      # Dictionary to store video paths and metadata
        self.favorites = {}    # Dictionary to store favorite videos
        self.personal = {}   # Dictionary to store video passwords

    def add_video(self, video_path,metadata):
        """Add a video to the library."""
        self.library.append(video_path)
        

    def list_videos(self):
        """List all videos in the library."""
        return 
    
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
