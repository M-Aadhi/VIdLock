# gui.py

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

         # Buttons for video management
        self.add_button = tk.Button(self.control_frame, text="Add Video", command=self.add_video)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.list_button = tk.Button(self.control_frame, text="List Videos", command=self.list_videos)
        self.list_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.details_button = tk.Button(self.control_frame, text="Video Details", command=self.show_video_details)
        self.details_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.favorite_button = tk.Button(self.control_frame, text="Mark as Favorite", command=self.mark_favorite)
        self.favorite_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.password_button = tk.Button(self.control_frame, text="Set Password", command=self.set_password)
        self.password_button.pack(side=tk.LEFT, padx=5, pady=5)

        

        

    def list_videos(self):
       return

    def play_selected_video(self, event):
        """Play the selected video."""
        return

    def show_video_details(self):
        """Show details of the selected video."""
        selected_video = self.listbox.get(tk.ACTIVE)
        if selected_video:
            metadata = self.video_manager.get_video_metadata(selected_video)
            if metadata:
                messagebox.showinfo("Video Details", f"Title: {metadata.get('title', 'N/A')}\n"
                                                      f"Duration: {metadata.get('duration', 'N/A')}\n"
                                                      f"Resolution: {metadata.get('resolution', 'N/A')}\n")
            else:
                messagebox.showwarning("Video Details", "No metadata available for the selected video.")


    def add_video(self):
        video_path = filedialog.askopenfilename()
        if video_path:
           metadata = {}  # Placeholder for metadata, can be obtained from the user or extracted from the video file
           self.video_manager.add_video(video_path, metadata)  
    def list_videos(self):
        videos = self.video_manager.list_videos()
        if videos:
            video_list = "\n".join(videos)
            messagebox.showinfo("Video Library", f"Videos in the library:\n{video_list}")
        else:
            messagebox.showinfo("Video Library", "No videos in the library.")

    def mark_favorite(self):
        video_path = filedialog.askopenfilename(title="Select Video File")
        if video_path:
            self.video_manager.mark_as_favorite(video_path)
            messagebox.showinfo("Success", "Video marked as favorite!")

    def set_password(self):
        video_path = filedialog.askopenfilename(title="Select Video File")
        if video_path:
            password = simpledialog.askstring("Password", "Enter password for the video:")
            if password:
                self.video_manager.set_password(video_path, password)
                messagebox.showinfo("Success", "Password set for the video!")
            else:
                messagebox.showwarning("Password", "Password cannot be empty!")

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


