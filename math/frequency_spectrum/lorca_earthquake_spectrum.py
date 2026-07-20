import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import g

def is_number(s):
    try:
        float(s)
    except ValueError:  # Failed
        return False
    else:  # Succeeded
        return True
    
inputDataFile= './LOR_20110511_164726.acc'

lorca_t= list()
lorca_a_norte= list()
lorca_a_este= list()
lorca_a_vert= list()
with open(inputDataFile, 'r') as f:
    for line in f:
        fields= line.split(' ')
        if(is_number(fields[0])):
            lorca_t.append(float(fields[0]))
            lorca_a_norte.append(float(fields[1])*g)
            lorca_a_este.append(float(fields[2])*g)
            lorca_a_vert.append(float(fields[3])*g)


t= np.array(lorca_t)
acceleration= np.array(lorca_a_vert)
dt= t[1]-t[0]
fs = 1 / dt # sampling frequency (Hz)
n_samples= len(t)

# 2. Compute the FFT
fft_values = np.fft.fft(acceleration)

# 3. Compute the frequencies with np.fft.fftfreq
# n_samples is the number of samples, and d is the time step.
frequencies = np.fft.fftfreq(n_samples, d=dt)

# 4. Obtener el espectro de amplitud unilateral (positivo)
# Por simetría, solo graficamos la primera mitad de la señal (hasta fs/2)
magnitude = np.abs(fft_values)[:n_samples // 2]
positive_frequencies = frequencies[:n_samples // 2]
magnitude = (2 / n_samples) * magnitude # Normalization to keep the real amplitude.


# 5. Visualización
plt.figure(figsize=(10, 5))
plt.plot(positive_frequencies, magnitude)
plt.title('Frequency spectrum of the accelerogram.')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Acceleration $(m/s^2)$')
plt.grid(True)
plt.show()
