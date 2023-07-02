import numpy as np
from math import sqrt, radians, cos, sin, log
from matplotlib import pyplot as plt

# coeff. of thrust
C_t = 0.8

# growth rate
k_s = 0.031

beta = 0.5 * (1 + sqrt(1 - C_t)) / sqrt(1 - C_t)

epsilon = sqrt(beta)


# diameter of the turbine in m
d_0 = 0.4

width = 15 # of simulation
height = 4 # of simulation
step = 0.01 # of simulation

yaw = radians(-30)

theta_c0 = 0.3 * yaw / cos(yaw) * (1 - sqrt(1 - C_t * cos(yaw)))
sigma_u0 = sqrt(C_t * (sin(yaw) + 1.978 * cos(yaw) * theta_c0) / (72 * theta_c0))

a = 0.166 * sqrt(C_t * cos(yaw))
b = sigma_u0

velocity = 6

def wake(X, Y):
    z = 1 - ((C_t * cos(yaw) / (16 * (k_s * X / d_0 + epsilon) ** 2)) * np.exp((-1 / (2 * (k_s * X / d_0 + epsilon) ** 2)) * ((Y - theta_c0 * X) / d_0) ** 2))

    return z * velocity

x, y = np.meshgrid(np.arange(0, width, step), np.arange(-height / 2, height / 2, step))

z = wake(x, y)

fig, ax = plt.subplots(1, 1)

plt.imshow(z, cmap='rainbow')
ax.set_title('Mathematical Wake Model')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
# plt.waitforbuttonpress()
