# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:49:17 2022

@author: pedro
"""

import numpy as np
import scipy.signal as sig
import splane as tc2
import matplotlib.pyplot as pl

wz = 3

num_pb = [1,0,wz**2]

den_pb = [1,2,2,1]

print('Transferencia pasabajo prototipo')
print('--------------------------------')
tc2.pretty_print_lti(num_pb, den_pb)