from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 1, 500)
triangle = signal.sawtooth(2 * np.pi * 5 * t, 0.5)
plt.plot(t, triangle)
plt.show()
