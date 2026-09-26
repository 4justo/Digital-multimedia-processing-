import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 44100
duration = 1.0

# Time array
t = np.arange(int(fs * duration)) / fs

# Generate sine waves
sine_440 = 0.5 * np.sin(2 * np.pi * 440 * t)
sine_220 = 0.5 * np.sin(2 * np.pi * 220 * t)
sine_880 = 0.5 * np.sin(2 * np.pi * 880 * t)

# Generate a square wave for comparison
square = 0.5 * np.sign(np.sin(2 * np.pi * 440 * t))

# Plot 440 Hz sine wave
plt.figure(figsize=(10, 5))
plt.plot(t[:300], sine_440[:300])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("440 Hz Sine Wave")
plt.grid(True)
plt.show()

# Compare frequencies
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t[:300], sine_220[:300])
plt.title("220 Hz Sine Wave")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t[:300], sine_440[:300])
plt.title("440 Hz Sine Wave")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t[:300], sine_880[:300])
plt.title("880 Hz Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()

# Compare sine and harmonically richer square wave
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t[:300], sine_440[:300])
plt.title("440 Hz Sine Wave")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t[:300], square[:300])
plt.title("440 Hz Square Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
