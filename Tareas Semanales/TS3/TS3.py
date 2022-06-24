# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 15:40:22 2022

@author: horay
"""

import numpy as np
import scipy.signal as sig
import splane as tc2
import matplotlib.pyplot as plt


# de la plantilla pasaaltos llegamos a la plantilla pasabajo
alfa_max = 1 # dB
alfa_min = 35
fs = 1000
fp = 3500

wp = fp * 2 * np.pi

ws = fs * 2 * np.pi/wp

wp_n= 1 #normalizada

# cuentas auxiliares

# epsilon 
ee = np.sqrt(10**(alfa_max/10)-1)

print (ee)

Om_p = 1
Om_s = 1/ws

for nn in range(2,6):
    alfa_min_w1 = 10*np.log10(1 + (ee**2) * (Om_s**2)**nn )
    print('con {:d} alfa minimo es {:f}'.format( nn, alfa_min_w1) )