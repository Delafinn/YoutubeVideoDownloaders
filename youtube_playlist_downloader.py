# Simple Youtube playlist downloader
import pytube
import downloader

# Loop indefinitely until the user exits
while True:
    # Print the prompt and ask the user for the YouTube playlist URL
    print('Enter the YouTube playlist URL')
    print('Example: https://www.youtube.com/watch?v=csO17lCKXIg&list=PLqwa-myoJ8QdXwCGew3vF7G0AAwinpYGl')
    url = input('URL: ')

    # Check if the user entered an empty URL or 'exit'
    if not url or url == 'exit':
        exit()

    # Create a Playlist object using the pytube library
    playlst = pytube.Playlist(url)

    # Print the playlist title and the video titles in the playlist
    print(f'Playlist title: {playlst.title}')
    print('The video titles in the playlist are:')
    for video in playlst.videos:
        print(video.title)

    # Ask the user if they want to download the playlist
    confirm_inp = input('Do you wish to download the playlist? [Y/N]: ').lower()
    # If the user does not want to download, exit the program
    if not confirm_inp or confirm_inp.startswith('n'):
        exit()

    # If the user wants to download, ask if they want to download the audio version only
    elif confirm_inp.startswith('y'):
        audio_q = input('Do you wish to download the audio version only? [y/N]: ').lower()

        # Ask the user where they want to save the download files
        path = input('Where do you want to save the download files? (Default is set to \'./out\'): ')
        # If the user did not specify a path, set the path to './out/<playlist_title>'
        path = f'./out/{playlst.title}' if not path else f'{path}/{playlst.title}'

        # If the user wants to download the audio version only, call the 'download_playlst_audio' function
        if audio_q.startswith('y'):
            downloader.download_playlst_audio(playlst, path)
            continue
        # If the user wants to download the video version, call the 'download_playlst_high_res' function
        downloader.download_playlst_high_res(playlst, path)
