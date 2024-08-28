import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cheby1, filtfilt

# Parâmetros do sinal
fs = 2000  # Frequência de amostragem em Hz
t = np.arange(0, 1.0, 1/fs)  # Vetor de tempo
f1, f2 = 50, 200  # Frequências dos sinais
x = 0.5 * np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)  # Sinal misto

# Projeto do filtro Chebyshev Tipo I
cutoff = 100  # Frequência de corte em Hz
rp = 20  # Ripple na banda passante (em dB)
order = 10  # Ordem do filtro

# Coeficientes do filtro
b, a = cheby1(order, rp, cutoff / (0.5 * fs), btype='low')

# Aplicação do filtro
y = filtfilt(b, a, x)

# Plotagem dos resultados
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x, label='Sinal Original')
plt.title('Sinal Original')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, y, label='Sinal Filtrado', color='orange')
plt.title('Sinal Filtrado com Chebyshev Tipo I')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()
plt.show()
