import cv2
import tkinter as tk
from PIL import Image, ImageTk
import vlc

class VideoPlayer:
    def __init__(self):
        self.instance = vlc.Instance('--no-xlib')
        self.player = self.instance.media_player_new()

    def load_video_on_canvas(self, video_path, canvas):
        self.media = self.instance.media_new(video_path)
        self.player.set_media(self.media)
        self.player.play()
        self.canvas = canvas
        self.update_canvas()

    def update_canvas(self):
        if self.player.is_playing():
            _, frame = self.player.video_get_size(0)
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = image.resize((self.canvas.winfo_width(), self.canvas.winfo_height()))
            photo = ImageTk.PhotoImage(image=image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.image = photo  # Keep a reference to prevent garbage collection
            self.canvas.after(33, self.update_canvas)  # Update every 33 milliseconds (30 frames per second)

    def play_video(self, video_path):
        media = self.instance.media_new(video_path)
        self.player.set_media(media)
        self.player.play()

    def load_video(self, video_path):
        media = self.instance.media_new(video_path)
        self.player.set_media(media)

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def rewind(self):
        current_time = self.player.get_time()
        self.player.set_time(max(0, current_time - 10000))  # rewind 10 seconds

    def forward(self):
        current_time = self.player.get_time()
        self.player.set_time(current_time + 10000)  # forward 10 seconds

    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        self.player.toggle_fullscreen()

    def set_volume(self, volume):
        self.player.audio_set_volume(volume)

    def set_position(self, position):
        self.player.set_position(position)

    def get_position(self):
        return self.player.get_position()

    def is_playing(self):
        return self.player.is_playing()
