from pytube import YouTube
import os

# Insert Youtube link list
music_list = []

for music in music_list:
    print(f'Starting download: {music}')

    yt = YouTube(music)

    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path="./musics")

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print('Download completed\n')
