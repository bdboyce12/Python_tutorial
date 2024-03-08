'''
This script attempts to plot A + Bcos(wt) using a function, and specifying A, B, and w as lists
'''

import numpy as np
import matplotlib.pyplot as plt

x_vals = np.arange(-10,10,0.1)

A = [1,2,3,4,5]
B = [5,4,3,2,1]
w = [1,3,5,7,9]

def plot(A,B,w):
    y_vals = A + B*np.cos(w*x_vals)

    plt.plot(x_vals, y_vals)
    plt.title(f'{A} + {B}cos({w}t)')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.show()

    return

for i in range(5):
    plot(A[i],B[i],w[i])
