'''
This script attempts to plot A + Bcos(wt) using a function, but by plotting each on the same graph
'''

import numpy as np
import matplotlib.pyplot as plt

x_vals = np.arange(-10,10,0.1)

A = [1,2,3]
B = [5,4,3]
w = [1,3,5]

def plot(A,B,w):
    y_vals = A + B*np.cos(w*x_vals)

    plt.plot(x_vals, y_vals)
    plt.title(f'${A} + {B}\cos({w}t)$')
    plt.xlabel('$x$')
    plt.ylabel('$y$')


    return

for i in range(3):
    plot(A[i],B[i],w[i])
plt.show()