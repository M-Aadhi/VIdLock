import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from video_player import VideoPlayer
from video_manager import VideoManager

class VidLockGUI:
    def __init__(self, root,video_manager=None):
        self.root = root
        self.video_manager = video_manager
        self.video_player = VideoPlayer()
        self.create_widgets()
    
    def create_widgets(self):
        self.video_frame = tk.Frame(self.root, bg='black')
        self.video_frame.pack(fill=tk.BOTH, expand=True)

        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(fill=tk.X)

        self.play_button = tk.Button(self.control_frame, text="Play Video", command=self.play_video)
        self.play_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.pause_button = tk.Button(self.control_frame, text="Pause Video", command=self.pause_video)
        self.pause_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.stop_button = tk.Button(self.control_frame, text="Stop Video", command=self.stop_video)
        self.stop_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.favorite_button = tk.Button(self.control_frame, text="Mark as Favorite", command=self.mark_favorite)
        self.favorite_button.pack(side=tk.LEFT, padx=5, pady=5)

         # Buttons for video management

        self.volume_label = tk.Label(self.control_frame, text="Volume")
        self.volume_label.pack(side=tk.LEFT, padx=5, pady=5)
        self.volume_slider = tk.Scale(self.control_frame, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_slider.set(50)
        self.volume_slider.pack(side=tk.LEFT, padx=5, pady=5)

        self.progress = ttk.Progressbar(self.control_frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
        self.progress.pack(side=tk.LEFT, padx=5, pady=5)

        self.library_button = tk.Button(self.control_frame, text="VidLock Library", command=self.open_library_window)
        self.library_button.pack(side=tk.LEFT, padx=5, pady=5)


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

    def list_videos(self):
        self.listbox.delete(0, tk.END)
        videos = self.video_manager.list_videos()
        for video in videos:
            self.listbox.insert(tk.END, video)

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

        add_video_button = tk.Button(self.library_window, text="Add Videos to Library", command=self.add_video)
        add_video_button.pack(pady=10)

        your_videos_button = tk.Button(self.library_window, text="Your Videos", command=self.list_videos)
        your_videos_button.pack(pady=10)

        fav_videos_button = tk.Button(self.library_window, text="Fav Videos", command=self.show_fav_videos)
        fav_videos_button.pack(pady=10)

        private_videos_button = tk.Button(self.library_window, text="Private Videos", command=self.show_private_videos)
        private_videos_button.pack(pady=10)

    
