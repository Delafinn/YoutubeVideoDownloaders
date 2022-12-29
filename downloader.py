import pytube

def download_high_res(video: pytube.YouTube, path: str) -> None:

    '''
        Downloads video with the highest resolution
    '''

    stream = video.streams.get_highest_resolution()
    stream.download(path)

    print(f'Video: {video.title} has been downloaded!')


def download_audio(video: pytube.YouTube, path: str) -> None:

    '''
        Downloads audio from youtube video
    '''

    stream = video.streams.get_audio_only()
    stream.download(path)

    print(f'Video: {video.title} has been downloaded!')


def download_playlst_high_res(playlist: pytube.Playlist, path: str) -> None:

    '''
        Download all video from the given playlist with the highest resolution  
    '''
    
    for vid in playlist.videos:
        vid.streams.get_highest_resolution().download(path)
        print(f"Video: {vid.title} has been downloaded!")

    print('Download complete!')


def download_playlst_audio(playlist: pytube.Playlist, path: str) -> None:
    
    '''
        Download all video from the given playlist as audio files.
    '''

    for vid in playlist.videos:
        vid.streams.get_audio_only().download(path)
        print(f"Video: {vid.title} has been downloaded!")

    print('Download complete!')