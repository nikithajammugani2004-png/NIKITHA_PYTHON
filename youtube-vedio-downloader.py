import yt_dlp
import tkinter as tk
from tkinter import filedialog
import os

def download_video(url, save_path):
    # Updated configuration to avoid the FFmpeg merge error
    ydl_opts = {
        # Downloads the best single MP4 file available (usually up to 720p)
        'format': 'best[ext=mp4]/best', 
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("\nFetching video information...")
            ydl.download([url])
        print("\nVideo downloaded successfully!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

def get_save_directory():
    # Initialize tkinter and hide the main window
    root = tk.Tk()
    root.withdraw()
    # Force the folder dialog to the top so it doesn't hide behind other windows
    root.attributes("-topmost", True)
    folder = filedialog.askdirectory(title="Select Download Folder")
    root.destroy()
    return folder

if __name__ == "__main__":
    video_url = input("Please enter the YouTube URL: ").strip()
    
    if not video_url:
        print("Error: URL cannot be empty.")
    else:
        save_dir = get_save_directory()
        if save_dir:
            print(f"Target folder: {save_dir}")
            download_video(video_url, save_dir)
        else:
            print("Download cancelled: No folder selected.")
