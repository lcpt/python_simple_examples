from scipy.interpolate import UnivariateSpline
import numpy as np
import matplotlib.pyplot as plt

xi= [-10.2422775, -9.7170325, -9.1917875, -8.6665425, -8.1412975, -7.6160525, -7.0908075, -6.5655625, -6.0403175, -5.5150725, -4.9898275, -4.4645825, -3.9393375, -3.4140925, -2.8888475, -2.3636025, -1.8383575, -1.3131125, -0.7878675, -0.2626225]
for x in reversed(xi):
    xi.append(-x)
    
wi= [54.94, 55.56, 56.72, 58.55, 61.02, 64.00, 67.22, 70.44, 73.66, 76.88, 80.10, 83.32, 86.54, 89.77, 92.99, 96.13, 98.96, 101.19, 102.72, 103.51]

for w in reversed(wi):
    wi.append(w)

    
interp_func = UnivariateSpline(xi, wi)

xxi= np.arange(xi[0], xi[-1], 0.1)
yyi= interp_func(xxi)

plt.plot(xxi, yyi)
plt.show()
