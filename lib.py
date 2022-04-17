from scipy.io import wavfile
import numpy as np


def comput_freq(file, start_time, end_time):
    sample_rate, data = wavfile.read(file)
    start_point = int(sample_rate * start_time / 1000)
    end_point = int(sample_rate * end_time / 1000)
    length = (end_time - start_time) / 1000
    counter = 0
    for i in range(start_point, end_point):
        if data[i] < 0 < data[i + 1]:
            counter += 1
    return counter / length


def sin_wav(duration, frequency, rate):
    t = np.linspace(0, duration, duration * rate, endpoint=False)
    x = np.sin(2 * np.pi * frequency * t)
    return x
