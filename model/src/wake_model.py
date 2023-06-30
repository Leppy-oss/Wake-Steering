import numpy as np
from math import sqrt
from matplotlib import pyplot as plt

# coeff. of thrust
C_t = 0.8

# growth rate
k_s = 0.031

beta = 0.5 * (1 + sqrt(1 - C_t)) / sqrt(1 - C_t)

epsilon = sqrt(beta)

width = 1000 # of simulation
height = 500 # of simulation

def wake(X, Y):
    z = np.cos(X / 2) + np.sin(X / 4)

    return z

x, y = np.meshgrid(np.arange(0, width, 1), np.arange(0, height, 1))

fig, ax = plt.subplots(1, 1)

cs = ax.contour(x, y, wake(x, y), 1)
ax.set_title('Mathematical Wake Model')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
# plt.waitforbuttonpress()
