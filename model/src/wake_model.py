import numpy as np
from math import sqrt, radians, cos, sin, log, degrees
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# coeff. of thrust
C_t = 0.8

# growth rate
k_s = 0.031

beta = 0.5 * (1 + sqrt(1 - C_t)) / sqrt(1 - C_t)

epsilon = sqrt(beta)


# diameter of the turbine in m
d_0 = 0.2

width = 50 * d_0 # of simulation
height = 10 * d_0 # of simulation
step = 0.005 # of simulation

yaw = radians(0.01)

theta_c0 = 0.3 * yaw / cos(yaw) * (1 - sqrt(1 - C_t * cos(yaw)))
sigma_u0 = sqrt(C_t * (sin(yaw) + 1.978 * cos(yaw) * theta_c0) / (72 * theta_c0))

a = 0.166 * sqrt(C_t * cos(yaw))
b = sigma_u0

velocity = 6

def wake(X, Y):
    z = 1 - ((C_t * cos(yaw) / (16 * (k_s * X / d_0 + epsilon) ** 2)) * np.exp((-1 / (2 * (k_s * X / d_0 + epsilon) ** 2)) * ((Y - theta_c0 * X) / d_0) ** 2))

    return z

x, y = np.meshgrid(np.arange(0, width, step), np.arange(-height / 2, height / 2, step))

z = wake(x, y)

fig, ax = plt.subplots(1)
plt.imshow(z, cmap='rainbow')
plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax.get_yticklabels(), visible=False)

# plt.axis('off');

# ax.set_xticks([0, 20, 40, 60, 80, 100])
# ax.set_xticklabels(['1', '2', '3', '4', '5', '6'])
# print(ax.get_xticklabels())
# plt.xticks(x_positions, [3, 3.5, 4, 4.5, 5])

yt = np.arange(0, height, step) # the grid to which your data corresponds
ny = yt.shape[0]
no_labels = 3 # how many labels to see on axis x
step_y = int(ny / (no_labels - 1)) # step between consecutive labels
y_positions = np.arange(0,ny,step_y) # pixel count at label position
y_positions
# plt.yticks(y_positions, [-0.5, 0.5])
# plt.yticks()
plt.title('Mathematical Wake Model')
# plt.xlabel('x')
# plt.ylabel('y')
plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# ax.set_title('Mathematical Wake Model')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.show()
fig.savefig('model/out/raw/wake_' + str(round(degrees(yaw))) + '_degrees.png')
# plt.waitforbuttonpress()
