import os

class VideoManager:
    def __init__(self):
        self.videos = {}

    def add_video(self, file_path):
        video_name = os.path.basename(file_path)
        self.videos[video_name] = file_path

    def get_video_list(self):
        return list(self.videos.keys())

    def get_video_path(self, video_name):
        return self.videos.get(video_name)
