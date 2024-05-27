import tkinter as tk
from tkinter import filedialog, messagebox ,ttk
from video_manager import VideoManager
from video_player import VideoPlayer
import threading

class VidLockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VidLock")
        self.canvas = tk.Canvas(self.root, width=640, height=480)
        self.canvas.pack()
        self.video_manager = VideoManager()
        self.video_player = VideoPlayer()  # Create an instance of the VideoPlayer class
        

        # Create GUI components
        self.create_widgets()
        self.create_player_controls()
        self.update_video_listbox()

        self.seek_bar_update_flag = True
        self.update_seek_bar()

    def create_widgets(self):
        # Add Video Button
        self.add_video_button = tk.Button(self.root, text="Add Video", command=self.add_video)
        self.add_video_button.pack()

        # Play Video Button
        self.play_video_button = tk.Button(self.root, text="Play Video", command=self.play_video)
        self.play_video_button.pack()

        # Video Canvas to display video frames
        self.video_canvas = tk.Canvas(self.root, width=640, height=480)
        self.video_canvas.pack()

        # Video Listbox
        self.video_listbox = tk.Listbox(self.root)
        self.video_listbox.pack()

        self.video_listbox.bind('<<Listboxselect>>',self.on_video_select)

    def add_video(self):
        file_path = filedialog.askopenfilename(title="Select a Video File", filetypes=[("Video files", "*.mp4 *.avi *.mkv")])
        if file_path:
            self.load_video(file_path)

    def load_video(self, video_path):
        self.video_player.load_video_on_canvas(video_path, self.canvas)

    def create_player_controls(self):
        controls_frame = tk.Frame(self.root)
        controls_frame.pack()

        # Play Button
        self.play_button = tk.Button(controls_frame, text="Play", command=self.play_video)
        self.play_button.grid(row=0, column=0)

        # Pause Button
        self.pause_button = tk.Button(controls_frame, text="Pause", command=self.pause_video)
        self.pause_button.grid(row=0, column=1)

        # Stop Button
        self.stop_button = tk.Button(controls_frame, text="Stop", command=self.stop_video)
        self.stop_button.grid(row=0, column=2)

        # Rewind Button
        self.rewind_button = tk.Button(controls_frame, text="<<", command=self.rewind_video)
        self.rewind_button.grid(row=0, column=3)

        # Forward Button
        self.forward_button = tk.Button(controls_frame, text=">>", command=self.forward_video)
        self.forward_button.grid(row=0, column=4)

        # Fullscreen Button
        self.fullscreen_button = tk.Button(controls_frame, text="Fullscreen", command=self.toggle_fullscreen)
        self.fullscreen_button.grid(row=0, column=5)

        # Volume Control
        self.volume_scale = tk.Scale(controls_frame, from_=0, to=100, orient=tk.HORIZONTAL, label="Volume")
        self.volume_scale.set(50)
        self.volume_scale.grid(row=0, column=3)
        self.volume_scale.bind("<Motion>", self.set_volume)

        # Seek Bar
        self.seek_bar = ttk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL)
        self.seek_bar.pack(fill=tk.X)
        self.seek_bar.bind("<ButtonRelease-1>", self.set_position)


    def on_video_select(self, event):
        if self.video_listbox.curselection():
            selected_video = self.video_listbox.get(self.video_listbox.curselection()[0])
            video_path = self.video_manager.get_video_path(selected_video)
            self.video_player.load_video(video_path)

    def add_video(self):
        file_path = filedialog.askopenfilename(title="Select a Video File", filetypes=[("Video files", "*.mp4 *.avi *.mkv")])
        if file_path:
            self.video_manager.add_video(file_path)
            self.update_video_listbox()

    def play_video(self):
        selected_video = self.video_listbox.get(tk.ACTIVE)
        if selected_video:
            video_path = self.video_manager.get_video_path(selected_video)
            self.video_player.play_video(video_path)
        else:
            messagebox.showwarning("No Video Selected", "Please select a video to play.")

    def pause_video(self):
        self.video_player.pause()

    def stop_video(self):
        self.video_player.stop()

    def rewind_video(self):
        self.video_player.rewind()

    def forward_video(self):
        self.video_player.forward()

    def toggle_fullscreen(self):
        self.video_player.toggle_fullscreen()

    def set_volume(self, event=None):
        volume = self.volume_scale.get()
        self.video_player.set_volume(volume)

    def set_position(self, event):
        position = self.seek_bar.get() / 100.0
        self.video_player.set_position(position)

    def update_video_listbox(self):
        self.video_listbox.delete(0, tk.END)
        for video in self.video_manager.get_video_list():
            self.video_listbox.insert(tk.END, video)

    def update_seek_bar(self):
        if self.video_player.is_playing():
            position = self.video_player.get_position() * 100
            self.seek_bar.set(position)
        self.root.after(1000, self.update_seek_bar)


if __name__ == "__main__":
    root = tk.Tk()
    app = VidLockApp(root)
    root.mainloop()
