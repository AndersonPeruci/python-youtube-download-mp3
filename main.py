import os

from pytube import YouTube
from moviepy.editor import *


def mp4_to_mp3(mp4, mp3):
    mp4_without_frames = AudioFileClip(mp4)
    mp4_without_frames.write_audiofile(mp3)
    mp4_without_frames.close()  # function call mp4_to_mp3("my_mp4_path.mp4", "audio.mp3")


# Insert YouTube link list
music_list = []

for music in music_list:
    print(f'Starting download: {music}')

    yt = YouTube(music)

    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path="musics")
    base, ext = os.path.splitext(out_file)

    mp4_to_mp3(f'{base}.mp4', f'{base}.mp3')

    # videoClip = VideoFileClip(os.path.join(f"{base}.mp4"))
    # video.audio.write_audiofile(os.path.join(base, ".mp3"))

    # base, ext = os.path.splitext(out_file)
    # new_file = base + '.mp3'
    # os.rename(out_file, new_file)

    print('Download completed\n')

# Old version
#
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
