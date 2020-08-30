"""Created on Sun Jul 12 14:47:03 2020.

@author: Veljko
"""

import pandas as pd
import numpy as np
import os
import random
import matplotlib.pyplot as plt
import glob
import scipy.io.wavfile as wav

mfcc_data_path = r"D:\obama_dataset\mfcc_new"
audio_data_path = r"D:\obama_dataset\audio_new"
mfcc_files = os.listdir(mfcc_data_path)
mfcc_file = random.choice(mfcc_files)
youtube_id = os.path.splitext(mfcc_file)[0]
audio_path = audio_data_path+os.sep+youtube_id+'.wav'
rate, audio_sig = wav.read(audio_path)
plt.figure()
plt.plot(np.linspace(start=0,
                     stop=len(audio_sig)/rate,
                     num=len(audio_sig)),
         audio_sig)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title(os.path.basename(audio_path),fontsize=8)
features = pd.read_csv(os.path.join(mfcc_data_path, mfcc_file))

i = 1
plt.figure()
features.plot(x='Timestamps', y='Cepstral%d'%i, legend=False)
plt.figure()
features.plot(x='Timestamps', y='Cepstral%d_delta'%i, legend=False)

i = 6
plt.figure()
features.plot(x='Timestamps', y='Cepstral%d'%i, legend=False)
plt.figure()
features.plot(x='Timestamps', y='Cepstral%d_delta'%i, legend=False)
i = 12
plt.figure()
features.plot(x='Timestamps', y='Cepstral%d'%i, legend=False)
plt.figure()
features.plot(x='Timestamps', y='Cepstral%d_delta'%i, legend=False)

i =1
plt.figure()
features['Cepstral%d'%i].plot.hist()

i =6
plt.figure()
features['Cepstral%d'%i].plot.hist()