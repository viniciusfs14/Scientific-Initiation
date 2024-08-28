import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Parâmetros do filtro
fs = 1000  # Frequência de amostragem em Hz
cutoff = 100  # Frequência de corte em Hz
numtaps = 1000  # Número de coeficientes do filtro

# Projeto do filtro FIR usando janela de Hamming
b = signal.firwin(numtaps, cutoff / (0.5 * fs), window='hamming')

# Gerar um sinal de exemplo (sinal composto por duas frequências)
t = np.arange(0, 1.0, 1/fs)  # Tempo de 1 segundo
x = 0.5 * np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 200 * t)  # Sinal com frequências 50 Hz e 200 Hz

# Aplicar o filtro ao sinal
y = signal.lfilter(b, 1.0, x)

# Plotar os resultados
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title('Sinal Original')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t, y)
plt.title('Sinal Filtrado')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

# Resposta em frequência do filtro
w, h = signal.freqz(b, worN=8000)

plt.subplot(3, 1, 3)
plt.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
plt.title('Resposta em Frequência do Filtro')
plt.xlabel('Frequência [Hz]')
plt.ylabel('Magnitude')
plt.grid()

plt.tight_layout()
plt.show()
