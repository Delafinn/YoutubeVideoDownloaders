"""simple Youtube video downloader"""
import time
import sys
from pytube import YouTube

while True:

    URL = input("""Enter the YouTube video URL\n
    Example: https://www.youtube.com/watch?v=dQw4w9WgXcQ \n:""")
    if URL in ("","exit"):
        sys.exit()

    yt = YouTube(URL)

    def high_res():
        """downloads highest resolution video"""
        stream = yt.streams.get_highest_resolution()
        stream.download(specify_directory)
        print(f"Video {yt.title.upper()} has been downloaded!")
        time.sleep(1.1)
        input("press any key to continue.")

    def audio_only():
        """downloads audio version"""
        stream = yt.streams.get_audio_only()
        stream.download(specify_directory)
        print(f"Video {yt.title.upper()} has been downloaded!")
        time.sleep(1.1)
        input("press any key to continue.")

    print(f"the video title is {yt.title.upper()}")
    download_q = input("Do you wish to download the video? ").lower()
    if download_q in ("no","n","","exit"):
        sys.exit()
    if download_q in ("yes","y"):

        specify_directory = input("Do you wish to specify the directory of the saved video? (Leave blank for the folder of the python script) ")
        audio_q = input("Do you wish to download the audio version only? ").lower()
        if audio_q in ("yes","y"):
            audio_only()
        else:
            high_res()
