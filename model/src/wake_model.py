import numpy as np
from math import sqrt, radians, cos, sin
from matplotlib import pyplot as plt

# coeff. of thrust
C_t = 0.8

# growth rate
k_s = 0.031

beta = 0.5 * (1 + sqrt(1 - C_t)) / sqrt(1 - C_t)

epsilon = sqrt(beta)

# diameter of the turbine in m
d_0 = 0.2

width = 15 # of simulation
height = 6 # of simulation
step = 0.05 # of simulation

yaw = radians(0)
velocity = 6

def wake(X, Y):
    z = 1 - ((C_t * cos(yaw) / (16 * (k_s * X / d_0 + epsilon) ** 2)) * np.exp((-1 / (2 * (k_s * X / d_0 + epsilon) ** 2)) * (Y / d_0) ** 2))

    return velocity - z

x, y = np.meshgrid(np.arange(0, width, step), np.arange(-height / 2, height / 2, step))

z = wake(x, y)

fig, ax = plt.subplots(1, 1)

plt.imshow(z, cmap='rainbow')
ax.set_title('Mathematical Wake Model')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
# plt.waitforbuttonpress()
