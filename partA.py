import numpy as np
import matplotlib.pyplot as plt
fs = 44100
duration = 2
frequency = 440
amplitude = 0.25
t = np.arange(int(fs * duration)) / fs
x = amplitude * np.sin(2 * np.pi * frequency * t)
print("Number of samples:", len(x))
print("Maximum amplitude:", np.max(x))
print("Minimum amplitude:", np.min(x))
plt.plot(t[:500], x[:500])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("440 Hz Sine Wave")
plt.grid(True)
plt.show()
