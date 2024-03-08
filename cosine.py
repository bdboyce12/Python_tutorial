'''
This script attempts to plot A + Bcos(wt) in a boring way
'''

import numpy as np
import matplotlib.pyplot as plt

A = 3
B = 1
w = 2

x_vals = np.arange(-10,10,0.1)
y_vals = A + B*np.cos(w*x_vals)

plt.plot(x_vals, y_vals)
plt.title(f'{A} + {B}cos({w}t)')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()