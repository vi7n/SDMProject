# import numpy as np
# import matplotlib.pyplot as plt

# number_of_states = 4
# all_state_data = []

# # Generate 5 elements
# for i in range(number_of_states):
#     # Compute the first row of the element
#     first_row = [i % 2, i // 2]
#     # Create the 2x2 matrix
#     element = [first_row, [f'({i}, 0)', f'({i}, 1)']]
#     # Add the element to the list
#     all_state_data.append(element)

# # Print the generated list
# print(all_state_data)

# fig, axs = plt.subplots(nrows=2, ncols=2)

# for i, element in enumerate(all_state_data):
#     # Get the x and y coordinates from the first row of the element
#     x, y = element[0]
#     # Get the value to show in the cell from the second row of the element
#     value = '\n'.join(element[1])
#     # Plot the element in the corresponding subplot
#     axs[y, x].text(0.5, 0.5, value, horizontalalignment='center', verticalalignment='center', fontsize=16)

# # Set the axis labels and title
# fig.suptitle('2x2 Matrix Plot')
# for ax in axs.flat:
#     ax.set(xlabel='X', ylabel='Y')

# # Hide the axis ticks and spines
# for ax in axs.flat:
#     ax.xaxis.set_visible(False)
#     ax.yaxis.set_visible(False)
#     ax.spines['top'].set_visible(False)
#     ax.spines['right'].set_visible(False)
#     ax.spines['bottom'].set_visible(False)
#     ax.spines['left'].set_visible(False)

# # Show the plot
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the number of states and the list to hold the data
number_of_states = 16
all_state_data = []

# Generate 16 elements
for i in range(number_of_states):
    # Compute the first row of the element
    first_row = [i % 4, (i // 4) % 4, i // 16]
    # Create the 2x3 matrix
    element = [first_row, [np.random.randint(0, 10) for _ in range(3)]]
    # Add the element to the list
    all_state_data.append(element)

# Print the generated list
print(all_state_data)

# Create a figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the elements in the 3D subplot
for i, element in enumerate(all_state_data):
    # Get the x, y, and z coordinates from the first row of the element
    x, y, z = element[0]
    # Get the value to show in the cell from the second row of the element
    value = element[1]
    # Compute the center coordinates of the cell
    cx, cy, cz = x + 0.5, y + 0.5, z + 0.5
    # Display the value at the center of the cell
    ax.text(cx, cy, cz, str(value), ha='center', va='center')
    
# Set the axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Matrix Plot')

# Show the plot
plt.show()

