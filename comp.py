import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, freqz, filtfilt

# Parâmetros do sinal
fs = 1000  # Frequência de amostragem em Hz
t = np.arange(0, 1.0, 1/fs)  # Vetor de tempo
f1, f2 = 50, 200  # Frequências dos sinais
x = 0.5 * np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)  # Sinal misto

# Parâmetros do filtro
cutoff = 100  # Frequência de corte em Hz
order = 10  # Ordem do filtro

# Projeto dos filtros
b_butter, a_butter = butter(order, cutoff / (0.5 * fs), btype='low')
b_cheby, a_cheby = cheby1(order, rp=1, Wn=cutoff / (0.5 * fs), btype='low')

# Frequência de resposta dos filtros
w_butter, h_butter = freqz(b_butter, a_butter, worN=8000, fs=fs)
w_cheby, h_cheby = freqz(b_cheby, a_cheby, worN=8000, fs=fs)

# Aplicação dos filtros
y_butter = filtfilt(b_butter, a_butter, x)
y_cheby = filtfilt(b_cheby, a_cheby, x)

# Plotagem dos resultados
plt.figure(figsize=(12, 10))

# Resposta em Frequência
plt.subplot(3, 1, 1)
plt.plot(w_butter, 20 * np.log10(np.abs(h_butter)), label='Butterworth')
plt.plot(w_cheby, 20 * np.log10(np.abs(h_cheby)), label='Chebyshev', linestyle='--')
plt.title('Resposta em Frequência')
plt.xlabel('Frequência [Hz]')
plt.ylabel('Magnitude [dB]')
plt.grid()
plt.legend()

# Sinal Original
plt.subplot(3, 1, 2)
plt.plot(t, x, label='Sinal Original')
plt.title('Sinal Original')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid()

# Sinal Filtrado
plt.subplot(3, 1, 3)
plt.plot(t, y_butter, label='Filtrado com Butterworth', color='orange')
plt.plot(t, y_cheby, label='Filtrado com Chebyshev', color='green', linestyle='--')
plt.title('Sinal Filtrado')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
