# video_player.py

import vlc

class VideoPlayer:
    def __init__(self):
        self.player = None
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

    def set_window(self, wm_id):
        self.player.set_hwnd(wm_id)

    def play(self, video_path):
        media = self.instance.media_new(video_path)
        self.player.set_media(media)
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def seek(self, position):
        self.player.set_time(position)
