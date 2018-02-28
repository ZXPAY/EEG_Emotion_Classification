# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 12:23:40 2018

@author: zxpay
"""

from FFT import FFT
from BandPassFilter import BandPassFilter
from scipy.signal import butter, lfilter, freqs
import numpy as np
import matplotlib.pyplot as plt
import time

t = np.linspace(0, 2, 256)
freq1 = 30
freq2 = 10
A1 = 4000
A2 = 5000
y = A1*np.sin(2*np.pi*freq1*t)
y2 = A2*np.sin(2*np.pi*freq2*t)
y3 = y+y2

plt.plot(t, y3, '*-')
plt.show()

Band_y = BandPassFilter(y3, 10, 50, 128, order=9)
Band_x = np.linspace(10,20,Band_y.shape[0])
plt.plot(Band_x, Band_y, '*-')
plt.show()

FFT_x, FFT_y = FFT(Band_y, 128, 128)
plt.plot(FFT_x, FFT_y, '*-')
plt.show()







   