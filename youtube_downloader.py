"""simple Youtube video downloader"""
import time
import sys
from pytube import YouTube


while True:

    URL = input("""Enter the YouTube video URL\n
    Example: https://www.youtube.com/watch?v=dQw4w9WgXcQ \n:""").lower()
    if URL in ("","exit"):
        sys.exit()
    yt = YouTube(URL)
    stream = yt.streams.get_highest_resolution()

    print(f"the video title is {yt.title.upper()}")
    download_q = input("Do you wish to download the video?").lower()
    if download_q in ("no","n"):
        sys.exit()
    if download_q in ("yes","y"):
        stream.download()
        print("Video has been downloaded!")
        time.sleep(1.1)
        input("press any key to continue.")
