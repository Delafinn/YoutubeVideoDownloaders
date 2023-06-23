import pytube

# Define a function named download_high_res that takes a YouTube video object and a path as input
def download_high_res(video: pytube.YouTube, path: str) -> None:
    '''
    Downloads video with the highest resolution
    '''
    # Retrieve the stream with the highest resolution for the provided YouTube video
    stream = video.streams.get_highest_resolution()
    
    # Download the video stream and save it to the specified path
    stream.download(path)
    
    # Print a message confirming the successful download, including the video title
    print(f'Video: {video.title} has been downloaded!')


# Define a function named download_audio that takes a YouTube video object and a path as input
def download_audio(video: pytube.YouTube, path: str) -> None:
    '''
    Downloads audio from YouTube video
    '''
    # Retrieve the audio-only stream of the provided YouTube video
    stream = video.streams.get_audio_only()
    
    # Download the audio stream and save it to the specified path
    stream.download(path)
    
    # Print a message confirming the successful download, including the video title
    print(f'Video: {video.title} has been downloaded!')


# Define a function named download_playlst_high_res that takes a YouTube playlist object and a path as input
def download_playlst_high_res(playlist: pytube.Playlist, path: str) -> None:
    '''
    Download all videos from the given playlist with the highest resolution
    '''
    # Iterate through each video in the playlist
    for vid in playlist.videos:
        # Retrieve the stream with the highest resolution for each video
        vid.streams.get_highest_resolution().download(path)
        
        # Print a message confirming the successful download, including the video title
        print(f"Video: {vid.title} has been downloaded!")

    # Print a message indicating the completion of the download
    print('Download complete!')


# Define a function named download_playlst_audio that takes a YouTube playlist object and a path as input
def download_playlst_audio(playlist: pytube.Playlist, path: str) -> None:
    '''
    Download all videos from the given playlist as audio files.
    '''
    # Iterate through each video in the playlist
    for vid in playlist.videos:
        # Retrieve the audio-only stream for each video
        vid.streams.get_audio_only().download(path)
        
        # Print a message confirming the successful download, including the video title
        print(f"Video: {vid.title} has been downloaded!")

    # Print a message indicating the completion of the download
    print('Download complete!')
