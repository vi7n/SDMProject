import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# create 5x5x5 grid
data = np.zeros((5, 5, 5))

# set coordinates for list 1 and list 2
list1 = [(1,1,1), (2,2,2), (3,3,3), (4,4,4), (0,4,4)]
list2 = [(0,0,0), (1,0,0), (2,0,0), (3,0,0), (4,0,0)]

# mark the coordinates in the data array
for coord in list1:
    data[coord] = 1
for coord in list2:
    data[coord] = 2

# create 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# plot the data for list 1 and list 2
x1, y1, z1 = np.array(list1).T
ax.scatter(x1, y1, z1, c='r', marker='o')
x2, y2, z2 = np.array(list2).T
ax.scatter(x2, y2, z2, c='b', marker='o')

# set axis labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.set_zlim(0, 4)

# show the plot
plt.show()
