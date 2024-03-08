'''
This script attempts to plot A + Bcos(wt) using a function
'''

import numpy as np
import matplotlib.pyplot as plt

x_vals = np.arange(-10,10,0.1)

A = float(input('What is your value of A?'))
B = float(input('What is your value of B?'))
w = float(input('What is your value of w?'))

def plot(A,B,w):
    y_vals = A + B*np.cos(w*x_vals)

    plt.plot(x_vals, y_vals)
    plt.title(f'{A} + {B}cos({w}t)')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.show()

    return

plot(A,B,w)
