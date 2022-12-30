# Simple Youtube video downloader
import pytube
import downloader

# Loop indefinitely until the user exits
while True:
    # Print the prompt and ask the user for the YouTube video URL
    print('Enter the YouTube video URL')
    print('Example: https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    url = input('URL: ')

    # Check if the user entered an empty URL or 'exit'
    if not url or url == 'exit':
        exit()

    # Create a YouTube object using the pytube library
    video = pytube.YouTube(url)
    print(f'Video title: {video.title}')

    # Ask the user if they want to download the video
    confirm_inp = input('Do you wish to download the video? [Y/N]: ').lower()
    # If the user does not want to download, exit the program
    if not confirm_inp or confirm_inp.startswith('n'):
        exit()

    # If the user wants to download, ask if they want to download the audio version only
    elif confirm_inp.startswith('y'):
        audio_q = input('Do you wish to download the audio version only? [Y/N]: ').lower()

        # Ask the user where they want to save the download files
        path = input('Where do you want to save the download files? (Default is set to \'./out\'): ')
        # If the user did not specify a path, set the path to './out'
        path = './out' if not path else path

        # If the user does not want to download the audio version only, call the 'download_high_res' function
        if not audio_q.startswith('y'):
            downloader.download_high_res(video, path)
            continue
        # If the user wants to download the audio version, call the 'download_audio' function
        downloader.download_audio(video, path)
