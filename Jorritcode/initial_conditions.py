# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:01:40 2016

@author: Jorrit
"""

import numpy as np

# Initial conditions
G = 6.67e-11
mp = 5.972e24
ms = 1.989e30
e = 0.0167
a = 1.496e11
q = mp / ms

xp = (1 - e) / (1 + q) * a
yp = 0

vpx = 0
vpy = (1 / (1 + q)) * np.sqrt((1 + e) / (1 - e)) * np.sqrt(( G * (mp + ms) ) / a)

xs = - q * xp
ys = - q * yp
vsx = - q * vpx
vsy = - q * vpy

dt = 36*24
N = 365000