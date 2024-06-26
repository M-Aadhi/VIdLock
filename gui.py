import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from video_player import VideoPlayer
from video_manager import VideoManager
from database import VideoDatabase
from PIL import Image, ImageTk
import os
import threading

class VidLockGUI:
    def __init__(self, root,video_manager):
        self.root = root
        self.video_frame = tk.Frame(self.root, bg='black')
        self.video_manager = VideoManager()
        self.video_player = VideoPlayer()
        self.video_db = VideoDatabase()
        self.create_widgets()
        self.bind_keys()

    def bind_keys(self):
        self.root.bind("<Left>", lambda event: self.seek_backward())
        self.root.bind("<Right>", lambda event: self.seek_forward())

    def seek_forward(self):
        current_time = self.video_player.get_time()
        new_time = current_time + 5000  # Seek forward 5 seconds
        self.video_player.set_time(new_time)

    def seek_backward(self):
        current_time = self.video_player.get_time()
        new_time = current_time - 5000  # Seek backward 5 seconds
        self.video_player.set_time(new_time)
    
    def create_widgets(self):
        
        style = ttk.Style(self.root)
        style.configure("TScale",
                background="black",
                troughcolor="gray",
                sliderthickness=20,
                relief="flat")


        self.video_frame = tk.Frame(self.root, bg='black')
        self.video_frame.pack(fill=tk.BOTH, expand=True)

        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(fill=tk.X)

        self.play_button = tk.Button(self.control_frame, text="Play Video", command=self.play_video)
        self.play_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.pause_button = tk.Button(self.control_frame, text="Pause Video", command=self.pause_video)
        self.pause_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.favorite_button = tk.Button(self.control_frame, text="Mark as Favorite", command=self.mark_favorite)
        self.favorite_button.pack(side=tk.LEFT, padx=5, pady=5)

         # Buttons for video management

        self.volume_label = tk.Label(self.control_frame, text="Volume")
        self.volume_label.pack(side=tk.LEFT, padx=5, pady=5)
        self.volume_slider = tk.Scale(self.control_frame, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_slider.set(50)
        self.volume_slider.pack(side=tk.LEFT, padx=5, pady=5)

        self.library_button = tk.Button(self.control_frame, text="VidLock Library", command=self.open_library_window)
        self.library_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.progress = ttk.Scale(self.control_frame, orient=tk.HORIZONTAL, length=700, from_=0, to=100, style="TScale", command=self.on_progress_change)
        self.progress.pack(side=tk.LEFT, padx=5, pady=5)

        self.backward_button = tk.Button(self.control_frame, text="<< Backward", command=self.seek_backward)
        self.backward_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.forward_button = tk.Button(self.control_frame, text="Forward >>", command=self.seek_forward)
        self.forward_button.pack(side=tk.LEFT, padx=5, pady=5)

    def on_progress_change(self, value):
        total_length = self.video_player.get_length()
        new_time = int(float(value) / 100 * total_length)
        self.video_player.set_time(new_time)

    def update_progress(self, progress):
        self.progress['value'] = progress * 100

    def set_volume(self, volume):
        self.video_player.set_volume(int(volume))

    def mark_favorite(self):
        video_path = filedialog.askopenfilename(title="Select Video File")
        if video_path:
            self.video_manager.mark_as_favorite(video_path)
            messagebox.showinfo("Success", "Video marked as favorite!")

    def play_video(self):
        video_path = filedialog.askopenfilename(title="Select Video File")
        if video_path:
            self.video_player.set_window(self.get_handle())
            self.video_player.play(video_path)

    def pause_video(self):
        self.video_player.pause()

    def stop_video(self):
        self.video_player.stop()

    def get_handle(self):
        return self.video_frame.winfo_id()
    
    def add_video(self):
        video_path = filedialog.askopenfilename()
        if video_path:
            metadata = {}  # Placeholder for metadata, can be obtained from the user or extracted from the video file
            self.video_manager.add_video(video_path, metadata)
            self.list_videos()

    def list_videos(self):
        for widget in self.library_window.winfo_children():
            widget.destroy()

        videos = self.video_manager.list_videos()
        for video in videos:
            video_path = video[1]
            title = video[2]
            thumbnail_path = video[5]
            self.add_video_to_library(video_path, thumbnail_path, title)


    def add_video_to_library(self, video_path, thumbnail_path, title):
        frame = tk.Frame(self.library_window)
        frame.pack(padx=10, pady=10)

        if thumbnail_path and os.path.exists(thumbnail_path):
            img = Image.open(thumbnail_path)
            img = img.resize((120, 90), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            label = tk.Label(frame, image=photo)
            label.image = photo
            label.pack(side=tk.LEFT)

        title_label = tk.Label(frame, text=title)
        title_label.pack(side=tk.LEFT, padx=10)
        title_label.bind("<Button-1>", lambda event, path=video_path: self.play_selected_video(path))

    def play_selected_video(self, video_path):
        self.video_player.set_window(self.get_handle())
        self.video_player.play(video_path)

    def show_fav_videos(self):
        fav_videos = self.video_manager.list_favorites()
        self.listbox.delete(0, tk.END)
        for video in fav_videos:
            self.listbox.insert(tk.END, video)

    def show_private_videos(self):
        private_videos = self.video_manager.list_private_videos()
        self.listbox.delete(0, tk.END)
        for video in private_videos:
            self.listbox.insert(tk.END, video)

    def open_library_window(self):
        self.library_window = tk.Toplevel(self.root)
        self.library_window.title("VidLock Library")
        self.library_window.geometry("800x600")

        add_video_button = tk.Button(self.library_window, text="Add Videos to Library", command=self.add_video)
        add_video_button.pack(pady=10)

        your_videos_button = tk.Button(self.library_window, text="Your Videos", command=self.list_videos)
        your_videos_button.pack(pady=10)

        fav_videos_button = tk.Button(self.library_window, text="Fav Videos", command=self.show_fav_videos)
        fav_videos_button.pack(pady=10)

        private_videos_button = tk.Button(self.library_window, text="Private Videos", command=self.show_private_videos)
        private_videos_button.pack(pady=10)

        

    
