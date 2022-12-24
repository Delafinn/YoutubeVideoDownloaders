"""Simple Youtube playlist downloader"""
import time
import sys
from pytube import Playlist

while True:

    URL = input("""Enter the playlist URL \n Example:
    https://www.youtube.com/watch?v=csO17lCKXIg&list=PLqwa-myoJ8QdXwCGew3vF7G0AAwinpYGl
    \n:""")
    if URL in ("","exit"):
        sys.exit()

    plylst = Playlist(URL)

    def download_plylst_audio():
        """downloads audio version"""
        for vid in plylst.videos:
            vid.streams.get_audio_only().download()
            print(f"video:{video.title} has been downloaded!")

    def download_plylst_highresolution():
        """downloads highest resolution video"""
        for vid in plylst.videos:
            vid.streams.get_highest_resolution().download()
            print(f"video:{video.title} has been downloaded!")


    print(f" the playlist title is: {plylst.title.upper()}")
    time.sleep(1)
    print("the video titles in the playlist are:")

    for video in plylst.videos:
        print(video.title)
        time.sleep(.1)

    download_q = input("Do you wish to download the playlist?\n:").lower()
    if download_q in ("no","n"):
        sys.exit()

    elif download_q in ("yes", "y"):
        audio_q = input("Do you want just the audio versions?\n:").lower()
        if audio_q not in ("yes","y"):
            download_plylst_audio()
        else:
            download_plylst_highresolution()
    else:
        print("invalid command")
        continue
