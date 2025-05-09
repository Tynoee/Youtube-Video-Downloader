import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_vid(url, path):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best', 
        'outtmpl': f'{path}/%(title)s.%(ext)s',  
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url]) 
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"Error: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    
    video_url = input("Please enter a Youtube url: ")
    save_dir = open_file_dialog()
    
    if save_dir:
        print("Started download...")
        download_vid(video_url, save_dir)
    else:
        print("Invalid save location.")
        