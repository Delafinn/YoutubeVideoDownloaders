import time
import pytube

def download_high_res(video: pytube.YouTube, path: str) -> None:

    '''
        Downloads video with the highest resolution
    '''

    stream = video.streams.get_highest_resolution()
    stream.download(path)

    print(f'Video {video.title.upper()} has been downloaded!')


def download_audio(video: pytube.YouTube, path: str) -> None:

    '''
        Downloads audio from youtube video
    '''

    stream = video.streams.get_audio_only()
    stream.download(path)

    print(f'Video {video.title.upper()} has been downloaded!')