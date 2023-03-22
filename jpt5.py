# import numpy as np

# # Create a 3-dimensional numpy array of size (80, 80, 80) with random True and False values
# arr = np.random.choice([True, False], size=(80, 80, 80))

# # Get the x, y, and z coordinates where the values are True
# x, y, z = np.where(arr)

# # Print the x, y, and z coordinates where the values are True
# for i in range(len(x)):
#     print("x:", x[i], "y:", y[i], "z:", z[i])

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate two lists of 3D coordinates
coords1 = np.random.rand(100, 3)
coords2 = np.random.rand(50, 3)

print(coords1)
print("----------------------------")
print(coords2)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the first set of coordinates as blocks
ax.scatter(coords1[:, 0], coords1[:, 1], coords1[:, 2], marker='s', s=50, color='b', alpha=0.5)

# Plot the second set of coordinates as circles
ax.scatter(coords2[:, 0], coords2[:, 1], coords2[:, 2], marker='o', s=50, color='r', alpha=0.5)

# Set the axis limits and labels
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
