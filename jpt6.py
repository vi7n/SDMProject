import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the lists of 3D coordinates
block_list = [(10, 20, 30), (40, 50, 60), (70, 80, 0)]
circle_list = [(5, 10, 15), (35, 45, 55), (65, 75, 20)]

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
