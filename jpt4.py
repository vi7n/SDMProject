import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.load(r'C:\Users\irobt\Desktop\SDMProject\occupancy.pkl.npy', allow_pickle=True)

# print(a)

# print(a.shape)

x, y, z = np.where(a)
obstacles = []
# Print the x, y, and z coordinates where the values are True
for i in range(len(x)):
    obstacles.append((x[i],y[i],z[i]))
    # print("x:", x[i], "y:", y[i], "z:", z[i])

path = [(4, 60, 22), (5, 60, 22), (5, 60, 22), (5, 61, 22), (5, 61, 23), (5, 62, 23), (5, 62, 23), (5, 62, 24), (6, 62, 24), (6, 63, 25), (6, 63, 25), (7, 63, 25), (7, 63, 26), (7, 64, 26), (8, 64, 26), (8, 64, 26), (8, 64, 27), (8, 65, 27), (9, 65, 27), (9, 65, 28), (9, 66, 27), (9, 66, 28), (10, 66, 28), (10, 66, 29), (10, 66, 29), (11, 66, 29), (11, 66, 30), (12, 66, 30), (12, 66, 31), (13, 66, 31), (14, 66, 31), (14, 66, 31), (15, 67, 31)]
print(obstacles)
# print(obstacles)

# Define the lists of 3D coordinates
block_list = obstacles
circle_list = path

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the block
block_x, block_y, block_z = zip(*block_list)
ax.scatter(block_x, block_y, block_z, marker='s', s=500)

# Plot the circles
circle_x, circle_y, circle_z = zip(*circle_list)
ax.scatter(circle_x, circle_y, circle_z, marker='o', s=100)

# Set the axis limits
ax.set_xlim([0, 80])
ax.set_ylim([0, 80])
ax.set_zlim([0, 80])

# Set the axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
