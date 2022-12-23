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

from pytube import YouTube
import os

music_list = [
    'https://www.youtube.com/watch?v=oYi_2oz9LAw',
    'https://www.youtube.com/watch?v=URE0riL21Dc',
    'https://www.youtube.com/watch?v=hlg4Zmt_I-Y',
    'https://www.youtube.com/watch?v=7djMIjhZOro',
    'https://www.youtube.com/watch?v=xcNn7Du1Ok4',
    'https://www.youtube.com/watch?v=dc6oADkbQSw',
    'https://www.youtube.com/watch?v=FE7Q950VptY',
    'https://www.youtube.com/watch?v=ROMqfy1uZbQ',
    'https://www.youtube.com/watch?v=jGd3V8lRqA4',
    'https://www.youtube.com/watch?v=xxBIdj3MX9U'
]

for music in music_list:
    print(f'Starting download: {music}')

    yt = YouTube(music)

    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path="./musics")

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print('Download completed\n')
