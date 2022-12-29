'''simple Youtube video downloader'''
import pytube
import downloader

while True:
    
    print('Enter the YouTube video URL')
    print('Example: https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    url = input('URL: ')

    if not url or url == 'exit':
        exit()

    video = pytube.YouTube(url)
    print(f'Video title: {video.title}')

    confirm_inp = input('Do you wish to download the video? [y/N]: ').lower()

    if not confirm_inp or confirm_inp.startswith('n'):
        exit()

    if confirm_inp.startswith('y'):

        audio_q = input('Do you wish to download the audio version only? [Y/N]: ').lower()

        path = input('Where do you want to save the download files? (Default is set to \'./out\'): ')
        path = './out' if not path else path
        
        if not audio_q.startswith('y'):
            downloader.download_high_res(video, path)
            continue

        downloader.download_audio(video, path)

