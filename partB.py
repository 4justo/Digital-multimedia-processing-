import numpy as np
import matplotlib.pyplot as plt

fs = 44100
t = np.arange(2 * fs) / fs

for frequency, amplitude in [(440, 0.5), (880, 0.5), (440, 0.25)]:
    x = amplitude * np.sin(2 * np.pi * frequency * t)

    print("Frequency:", frequency, "Hz")
    print("Amplitude:", amplitude)
    print("Samples:", len(x))
    print("Max:", np.max(x))
    print("Min:", np.min(x))

    plt.plot(t[:500], x[:500])
    plt.title(f"{frequency} Hz, Amplitude {amplitude}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()
