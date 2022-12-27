import os
from pytube import YouTube
from moviepy.editor import *


def mp4_to_mp3(mp4, mp3):
    mp4_without_frames = AudioFileClip(mp4)
    mp4_without_frames.write_audiofile(mp3)
    mp4_without_frames.close()  # function call mp4_to_mp3("my_mp4_path.mp4", "audio.mp3")


# Insert YouTube link list
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
    out_file = video.download(output_path="musics")
    base, ext = os.path.splitext(out_file)

    mp4_to_mp3(f'{base}.mp4', f'{base}.mp3')

    # videoClip = VideoFileClip(os.path.join(f"{base}.mp4"))
    # video.audio.write_audiofile(os.path.join(base, ".mp3"))

    # base, ext = os.path.splitext(out_file)
    # new_file = base + '.mp3'
    # os.rename(out_file, new_file)

    print('Download completed\n')
