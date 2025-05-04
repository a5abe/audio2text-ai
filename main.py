# main.py

# This script loads an audio file, extracts its pitch over time using librosa,
# and visualizes the estimated pitch (frequency in Hz) over time.
# Intended for beginners and those exploring how to analyze music/audio programmatically.

import librosa  # Library for audio processing
import librosa.display  # For waveform and spectrogram display
import matplotlib.pyplot as plt  # For plotting graphs
import numpy as np  # For numerical processing

# === Step 1: Load audio file ===
# Replace "output.wav" with your own WAV file name if needed.
filename = "output.wav"

# Load audio as a waveform `y`, and get its sampling rate `sr`
# y: waveform (1D numpy array), sr: sampling rate (samples per second)
y, sr = librosa.load(filename)

# === Step 2: Estimate pitch (frequency) over time ===
# `piptrack` returns pitch and magnitude arrays
# pitches: estimated pitches [frequency], magnitudes: corresponding strength (loudness)
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

# === Step 3: Extract dominant pitch for each frame ===
# We'll pick the pitch with the highest energy in each time frame
pitch_values = []
for i in range(pitches.shape[1]):
    index = magnitudes[:, i].argmax()  # Find index with max magnitude in this frame
    pitch = pitches[index, i]  # Get pitch at that index
    if pitch > 0:
        pitch_values.append(pitch)
    else:
        pitch_values.append(np.nan)  # Use NaN for silence/gap (for cleaner graph)

# === Step 4: Create time axis for plotting ===
# We'll generate a timeline that matches the number of pitch values
times = np.linspace(0, len(pitch_values) / sr, num=len(pitch_values))

# === Step 5: Plot pitch over time ===
plt.figure(figsize=(12, 4))
plt.plot(times, pitch_values, label="Pitch (Hz)", color="tab:blue")
plt.title("Estimated Pitch Over Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency (Hz)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
