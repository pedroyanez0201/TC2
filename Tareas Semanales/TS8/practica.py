#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Módulos importantantes
import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt
from splane import plot_plantilla


fs = 1000 # Hz
nyq_frec = fs / 2

ripple = 0 # dB
atenuacion = 40 # dB

ws1 = 1.0 #Hz
wp1 = 3.0 #Hz
wp2 = 25.0 #Hz
ws2 = 35.0 #Hz

frecs = np.array([0.0,         ws1,         wp1,     wp2,     ws2,         nyq_frec   ]) / nyq_frec
gains = np.array([-atenuacion, -atenuacion, -ripple, -ripple, -atenuacion, -atenuacion])
gains = 10**(gains/20)

# bp_sos_butter = sig.iirdesign([wp1, wp2], [ws1, ws2], 0.1, 40, False, 'cheby2', 'sos', 1000)

# Si bien me piden 40dB de atenuacion en las ws, lo que hago es atenuar 41 subir el grafico en 1
# db, asi nunca entra el filtro en las zonas prohibidas
bp_sos_butter = sig.iirdesign([wp1, wp2], [ws1, ws2], 0.1, 41, False, 'cheby2', 'sos', 1000)

w_rad  = np.append(np.logspace(-2, 0.8, 250), np.logspace(0.9, 1.6, 250) )
w_rad  = np.append(w_rad, np.linspace(40, nyq_frec, 500, endpoint=True) ) / nyq_frec * np.pi

_, butter = sig.sosfreqz(bp_sos_butter, w_rad)

# plt.plot((w_rad/np.pi)*500, 20*np.log10(np.abs(butter)+1e-12))

# Levanto el grafico en 1dB
plt.plot((w_rad/np.pi)*500, 20*np.log10(np.abs(butter)+1e-12)+1)
plt.grid()

# Plantilla
plot_plantilla(filter_type = 'bandpass', fpass = frecs[[2, 3]]* nyq_frec, ripple = ripple , fstop = frecs[ [1, 4] ]* nyq_frec, attenuation = atenuacion, fs = fs)
