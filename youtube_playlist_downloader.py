'''Simple Youtube playlist downloader'''
import pytube
import downloader

while True:
    
    print('Enter the YouTube playlist URL')
    print('Example: https://www.youtube.com/watch?v=csO17lCKXIg&list=PLqwa-myoJ8QdXwCGew3vF7G0AAwinpYGl')

    url = input('URL: ')

    if not url or url == 'exit':
        exit()

    playlst = pytube.Playlist(url)

    print(f'Playlist title: {playlst.title}')
    print('The video titles in the playlist are:')

    for video in playlst.videos:
        print(video.title)

    confirm_inp = input('Do you wish to download the video? [y/N]: ').lower()

    if not confirm_inp or confirm_inp.startswith('n'):
        exit()

    elif confirm_inp.startswith('y'):

        audio_q = input('Do you wish to download the audio version only? [y/N]: ').lower()

        path = input('Where do you want to save the download files? (Default is set to \'./out\'): ')
        path = f'./out/{playlst.title}' if not path else f'{path}/{playlst.title}'

        if not audio_q.startswith('y'):
            downloader.download_playlst_audio(playlst, path)
            continue

        downloader.download_playlst_high_res(playlst, path)