import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# create 5x5x5 grid with diagonal elements colored
data = np.zeros((5, 5, 5))
for i in range(5):
    data[i,i,i] = 1

# create 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# plot the data
x, y, z = np.indices((5, 5, 5))
ax.scatter(x.flatten(), y.flatten(), z.flatten(), c=data.flatten(), marker='o')

# set axis labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.set_zlim(0, 4)

# show the plot
plt.show()
