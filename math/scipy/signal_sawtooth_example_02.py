from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 1, 500)
numberOfCycles= 1.5
amplitude= .02
triangle = amplitude*signal.sawtooth(2 * np.pi * numberOfCycles * t, 0.5)
plt.plot(t, triangle)
plt.show()
