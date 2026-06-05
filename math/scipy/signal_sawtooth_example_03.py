from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 1, 500)
numberOfCycles= 1.0
amplitude= .02
phase= 0.25
triangle = amplitude*signal.sawtooth(2 * np.pi * numberOfCycles * t+ 2 * np.pi * phase, 0.5)

plt.plot(t, triangle)
plt.show()
