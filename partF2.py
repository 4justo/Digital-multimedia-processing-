import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 44100
duration = 1.0

t = np.arange(int(fs * duration)) / fs

# Fundamental and harmonics
fundamental = 0.5 * np.sin(2 * np.pi * 440 * t)
harmonic2 = 0.25 * np.sin(2 * np.pi * 880 * t)
harmonic3 = 0.125 * np.sin(2 * np.pi * 1320 * t)

# Combine the signals
additive = fundamental + harmonic2 + harmonic3

# Plot fundamental
plt.figure(figsize=(10, 5))
plt.plot(t[:300], fundamental[:300])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("440 Hz Fundamental")
plt.grid(True)
plt.show()

# Plot additive signal
plt.figure(figsize=(10, 5))
plt.plot(t[:300], additive[:300])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Additive Synthesis: 440 + 880 + 1320 Hz")
plt.grid(True)
plt.show()

# Compare them
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t[:300], fundamental[:300])
plt.title("Fundamental: 440 Hz")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t[:300], additive[:300])
plt.title("Combined Additive Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
