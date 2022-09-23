# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 18:09:48 2022

@author: horay
"""

import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

fc = 1e3
fs = 100e3
xlim1=0
xlim2=10
ylim1=-60
ylim2=4
    
WN = int(5*10e3) # Cantidad de puntos para la funcion Freqz
KHz = 1000
  # Frecuencia de corte del filtro
  # fc = 1e3
wc = 2*np.pi*fc
  # Frecuencia de Sampling
  # fs = 100e3
nq = fs/2
#  ws = 2*np.pi*fs
  
#Normalizacion de las Fs
fs_n = fs/wc
#ws_n = ws/W_fc
  
  # K de transormada Bilineal
K = 2*fs_n
  # Q de Butter Orden 2
Q = np.sqrt(2)/2
  
  # Coeficientes desnormalizados
A = 1
B = 2
C = 1
  
D= K**2 + K/Q + 1
E = 2 - 2*K**2
F = K**2 - K/Q + 1
  
  
  
  #Coeficientes normalizados
a0 = 1
a1 = E/D
a2 = F/D
  
b0 = A/D
b1 = B/D
b2 = C/D

print ("a0", a0)
print ("a1", a1)
print ("a2", a2)
print ("b0", b0)
print ("b1", b1)
print ("b2", b2)

  
numz = [b0, b1, b2]
denz = [a0, a1, a2]
  
w, h = sig.freqz(numz,denz,WN)
  
  # simulacion python
num_lp = [0,  0,  1]
den_lp = [1, 1/Q, 1]
  
numz_py, denz_py = sig.bilinear(num_lp, den_lp, fs_n) 
w_py, h_py = sig.freqz(numz_py,denz_py,WN)
  
  # filtro analogico
  # w_analog, h_analog = sig.freqs(num_lp,den_lp)
w_analog, h_analog = sig.freqs(num_lp,den_lp,  worN=np.logspace(-3, 2, 1000))
h_analog_db    = 20*np.log10(np.maximum(np.abs(h_analog), 1e-4))
  
h_db    = 20*np.log10(np.maximum(np.abs(h), 1e-4))
h_db_py = 20*np.log10(np.maximum(np.abs(h_py), 1e-4))
  
  # Grafico
fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True)
fig.set_size_inches(16,12)
  # MODULO
fig.suptitle('ButterWorth N=2')
ax.plot(w*nq/(np.pi*KHz), h_db,linewidth=3, label = 'Calculado')
ax.plot(w_py*nq/(np.pi*KHz), h_db_py,color='purple',linestyle='dashed',linewidth=3, label = 'Python')
ax.plot(w_analog*fc/KHz, h_analog_db, color = 'orange',linestyle=':',  linewidth=3, label = 'Analogico')
ax.grid(True)
ax.set_title('Respuesta Magnitud $f_c = {} KHz$ | $f_s = {}KHz$'.format(fc/KHz, fs/KHz))
ax.set_ylabel('Magnitud [dB]')
ax.set_xlabel('Frecuencia [KHz]')
ax.legend()
ax.set_xlim([xlim1, xlim2])
ax.set_ylim([ylim1, ylim2])
  
  # # descomentar para ver los graficos en la frecuencia de corte
  
  # # atenuacion 3db en fc = 1KHz
  # ax.set_xlim([0, 2])
  # ax.set_ylim([-14, 3])
  # ax.set_xticks([0, 0.5, 1, 1.5, 2])
  # ax.set_xticklabels(['0', '0.5','$f_c = 1$','1.5','2'])
  # ax.set_yticks([-12, -9, -6, -3, 0, 3])     



