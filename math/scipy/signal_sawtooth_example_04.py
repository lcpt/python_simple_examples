import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Time array: 1 second, 500 samples
t = np.linspace(0, 1, 500)
freq = 5  # 5 Hz frequency

# 1. Standard sawtooth (phase = 0)
saw_standard = signal.sawtooth(2 * np.pi * freq * t)

# 2. Sawtooth with a 25% (0.25) phase shift
saw_shifted = signal.sawtooth(2 * np.pi * freq * t + 2 * np.pi * 0.25)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(t, saw_standard, label='Standard (phase=0)', color='blue')
plt.plot(t, saw_shifted, label='Shifted (phase=0.25)', color='orange', linestyle='--')

plt.title('Scipy.signal.sawtooth Phase Example')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.axhline(0, color='black', linewidth=0.8)
plt.legend()
plt.grid(True)
plt.show()
