import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 44100
duration = 1.0

t = np.arange(int(fs * duration)) / fs

# 440 Hz tone
tone = 0.5 * np.sin(2 * np.pi * 440 * t)

# ADSR parameters
attack = int(0.10 * fs)
decay = int(0.15 * fs)
release = int(0.20 * fs)

sustain_end = len(tone) - release

# Create envelope
env = np.ones(len(tone))

# Attack
env[:attack] = np.linspace(0, 1, attack)

# Decay
env[attack:attack + decay] = np.linspace(1, 0.7, decay)

# Sustain
env[attack + decay:sustain_end] = 0.7

# Release
env[sustain_end:] = np.linspace(0.7, 0, release)

# Apply envelope
shaped = tone * env

# Display envelope
plt.figure(figsize=(10, 5))
plt.plot(t, env)
plt.xlabel("Time (s)")
plt.ylabel("Envelope Level")
plt.title("ADSR-style Amplitude Envelope")
plt.grid(True)
plt.show()

# Display original tone
plt.figure(figsize=(10, 5))
plt.plot(t[:1000], tone[:1000])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Original 440 Hz Tone")
plt.grid(True)
plt.show()

# Display shaped tone
plt.figure(figsize=(10, 5))
plt.plot(t[:1000], shaped[:1000])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("440 Hz Tone with ADSR Envelope")
plt.grid(True)
plt.show()
