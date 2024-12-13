from pytube import YouTube
from sys import argv
import os

if len(argv) < 2:
    print("Usage: python yt.py <YouTube URL>")
    exit(1)

link = argv[1]
try:
    yt = YouTube(link)
    
    # Try to get the highest resolution progressive stream
    yd = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    
    if yd is None:
        print("No suitable stream found.")
        exit(1)
    
    download_path = r"D:\Down games\videos"
    
    # Ensure the download directory exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    yd.download(download_path)
    print("Download completed!")
except Exception as e:
    print(f"An error occurred: {e}")