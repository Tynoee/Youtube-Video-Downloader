from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_vid(url, path):
    try:
        yt = Youtube(url)
        streams = yt.streams.filter(progressive = True, file_extension = "mp4")
        highest_res_stream = streams.get_highest_res
    
    except Exception as e:
        print(e)
        