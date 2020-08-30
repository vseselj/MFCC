"""Created on Thu Jul  9 21:48:17 2020.

@author: Veljko
"""
# 3rd party libs
from python_speech_features import mfcc
from python_speech_features import fbank
from python_speech_features import delta
# built-in libs
import scipy.io.wavfile as wav
import pandas as pd
import numpy as np
import glob
import os


# MFCC parameteres
winlen = 0.025  # length of analysis window in seconds
winstep = 0.01  # the step between successive windows in seconds
nfilt = 40  # the number of filters in the filterbank
lowfreq = 133.333  # lowest band edge of mel filters in Hz
highfreq = 6855.4976  # highest band edge of mel filters in Hz
ncep = 13  # the number of cepstrum coefficients

# paths
audio_data_path = r"D:\obama_dataset\audio_new\normalized"
mfcc_data_path = r"D:\obama_dataset\mfcc_new"
youtube_ids = os.listdir(audio_data_path)

for youtube_id in youtube_ids:
    youtube_id = os.path.splitext(youtube_id)[0]
    save_file = os.path.join(mfcc_data_path, youtube_id+".csv")
    if os.path.isfile(save_file):
        os.remove(save_file)
    audio_path = os.path.join(audio_data_path, youtube_id)+r".wav"
    rate, audio_sig = wav.read(audio_path)
    mfcc_feat = mfcc(audio_sig,
                     rate,
                     winlen=winlen,
                     winstep=winstep,
                     numcep=ncep,
                     nfilt=nfilt,
                     lowfreq=lowfreq,
                     highfreq=highfreq,
                     ceplifter=0,
                     appendEnergy=True,
                     winfunc=np.hamming)
    delta_feat = delta(mfcc_feat, N=2)
    timestamps = []
    for i in range(mfcc_feat.shape[0]):
        start_time = i * winstep
        end_time = min(len(audio_sig)*rate, start_time+winlen)
        timestamps.append((start_time+end_time)/2)
    columns = []
    columns.append("Energy")
    for i in range(1, ncep):
        columns.append("Cepstral%d" % i)
    columns.append("Energy_delta")
    for i in range(1, ncep):
        columns.append("Cepstral%d_delta" % i)
    features = pd.DataFrame(data=np.c_[mfcc_feat, delta_feat],
                            index=timestamps,
                            columns=columns)
    features.index.name = "Timestamps"
    features.to_csv(save_file)
