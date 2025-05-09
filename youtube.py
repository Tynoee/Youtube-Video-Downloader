import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_vid(url, path):
    # Options for downloading video
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Get the best video + best audio
        'outtmpl': f'{path}/%(title)s.%(ext)s',  # Specify the download path and filename
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Download the video
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example URL and download path
url = "https://www.youtube.com/watch?v=B9YYkGheG0M"
path = "C:/Users/Admin/Desktop/Repositories/python/Youtube-Video-Downloader"

download_vid(url, path)

# def open_file_dialog():
#     folder = filedialog.askdirectory()
#     if folder:
#         print(f"Selected folder: {folder}")
#     pass


# if __name__ == "__main__":
#     root = tk.Tk()
#     root.withdraw()
    
#     video_url = input("Please enter a Youtube url: ")
#     save_dir = open_file_dialog()
    
#     if save_dir:
#         print("Started download...")
#         download_vid(video_url, save_dir)
#     else:
#         print("Invalid save location.")
        