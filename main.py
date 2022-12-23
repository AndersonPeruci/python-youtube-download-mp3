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

# from __future__ import unicode_literals
# import youtube_dl
#
# link = input("Insert the link")
#
# ydl_opts = {
#     'format': 'bestaudio/best',
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '320',
#     }],
#     'prefer_ffmpeg': True,
# }
#
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([link])
#
# print("Contact me on discord for any problem: https://discord.gg/BgjwgWx")
