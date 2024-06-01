# video_player.py

import vlc
import time
import threading
import os

class VideoPlayer:
    def __init__(self):
        self.player = None
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.is_playing = False
        self.update_thread = None

    def set_window(self, wm_id):
        self.player.set_hwnd(wm_id)

    def play(self, video_path):
        media = self.instance.media_new(video_path)
        self.player.set_media(media)
        self.player.play()
        self.is_playing = True
        self.start_update_thread()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()
        self.is_playing = False

    def set_volume(self, volume):
        self.player.audio_set_volume(volume)

    def get_volume(self):
        return self.player.audio_get_volume()

    def get_length(self):
        return self.player.get_length()

    def get_time(self):
        return self.player.get_time()

    def set_time(self, time_ms):
        self.player.set_time(time_ms)

    def start_update_thread(self):
        if self.update_thread is None:
            self.update_thread = threading.Thread(target=self.update_progress)
            self.update_thread.start()

    def update_progress(self):
        while self.is_playing:
            time.sleep(1)
            current_time = self.get_time()
            total_length = self.get_length()
            if total_length > 0:
                progress = current_time / total_length
                if self.progress_callback:
                    self.progress_callback(progress)  # Call the progress callback function

    def set_progress_callback(self, callback):
        self.progress_callback = callback

    def seek(self, position):
        self.player.set_time(position)
