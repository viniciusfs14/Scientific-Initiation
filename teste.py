from scipy.signal import ellip, filtfilt
import numpy as np

# Especificações do filtro
ordem = 4           # Ordem do filtro
rp = 1              # Ondulação máxima na banda de passagem (em dB)
rs = 40             # Atenuação mínima na banda de rejeição (em dB)
f_pass = 0.2        # Frequência de corte da banda de passagem (normalizada)
f_stop = 0.3        # Frequência de corte da banda de rejeição (normalizada)

# Gerar um sinal
t = np.arange(0, 1.0, 1/fs)  # Tempo de 1 segundo
x = 0.5 * np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 200 * t)  # Sinal com frequências 50 Hz e 200 Hz

# Design do filtro elíptico
b, a = ellip(ordem, rp, rs, f_pass, btype='low', analog=False)

# Aplicação do filtro a um sinal de exemplo
sinal_filtrado = filtfilt(b, a, sinal)

