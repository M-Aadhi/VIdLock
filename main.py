import tkinter as tk
from tkinter import*
from tkinter import filedialog, messagebox ,ttk
from gui import VidLockGUI
from video_manager import VideoManager
from video_player import VideoPlayer

class VidLockApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.state('zoomed')
        self.root.title("VidLock")
        self.video_manager = VideoManager() 
        self.video_player =VideoPlayer()
        self.gui = VidLockGUI(self.root,self.video_manager)
       
        
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = VidLockApp()
    app.run() 
