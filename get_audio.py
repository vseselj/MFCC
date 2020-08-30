"""Created on Sat Jul  4 12:26:31 2020.

@author: Veljko
(basic script info).
"""

import os
import glob
import subprocess

video_data_path = "D:\\obama_dataset\\video"
audio_data_path = "D:\\obama_dataset\\audio"
video_directories = os.listdir(video_data_path)
for directory in video_directories:
    try:
        os.mkdir(audio_data_path+'\\'+directory)
    except OSError:
        pass
    video_path = glob.glob(video_data_path+'\\'+directory+'\\*.mp4')
    if len(video_path) != 1:
        raise ValueError("Video file not found")
    else:
        video_path = video_path[0]
    audio_path = video_path.replace("video", "audio")
    audio_path, _ = os.path.splitext(audio_path)
    audio_path = audio_path + ".wav"
    command = 'ffmpeg -i "{}" -ar 16000 -ac 1 -f wav -acodec pcm_f32le "{}"'.format(video_path,
                                                                  audio_path)
    subprocess.run(command)
