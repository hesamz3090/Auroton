import numpy as np
from scipy.io import wavfile
from scipy.io.wavfile import read
import wave
import sys
import matplotlib.pyplot as plt

start = 0
end = 10
time = 5
rate = 52800
file = 'output.wav'

t = np.linspace(start, end, rate * time)

x1 = np.sin(400 * t)
x2 = np.sin(800 * t)

z = np.append(x1, x2)
wavfile.write(file, rate, z)



input_data = read(file)
audio = input_data[1]
plt.plot(audio[0:1024*10])
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.show()
