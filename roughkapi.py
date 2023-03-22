import numpy as np
import matplotlib.pyplot as plt

# n = 5 #number of states
# a = np.zeros((n,2,2))
# a[0,0,0] = 1
# print(a[0])
number_of_states = 20
all_state_data = []


for i in range(number_of_states):
    # Compute the first row of the element
    first_row = [i % 5, i // 5]
    # Create the 2x2 matrix
    element = [first_row, [1, 1]]
    # Add the element to the list
    all_state_data.append(element)

# Print the generated list
print(all_state_data)

fig, axs = plt.subplots(nrows=4, ncols=5)
# all_state_data[0][1] = [0,0]
# all_state_data[19][1] = [0.5,0.5]
# for i, element in enumerate(all_state_data):
#     # Get the x and y coordinates from the first row of the element
#     x, y = element[0]
#     # Get the value to show in the cell from the second row of the element
#     value = element[1]
#     # Plot the element in the corresponding subplot
#     axs[y, x].imshow(np.array([value]), cmap='gray')

# # Set the axis labels and title
# fig.suptitle('2x2 Matrix Plot')
# for ax in axs.flat:
#     ax.set(xlabel='X', ylabel='Y')

# # Show the plot
# plt.show()

for i, element in enumerate(all_state_data):
    # Get the x and y coordinates from the first row of the element
    x, y = element[0]
    # Get the value to show in the cell from the second row of the element
    value = element[1]
    # Plot the element in the corresponding subplot
    axs[y, x].text(0.5, 0.5, value, horizontalalignment='center', verticalalignment='center', fontsize=16)

# Set the axis labels and title
fig.suptitle('2x2 Matrix Plot')
for ax in axs.flat:
    ax.set(xlabel='X', ylabel='Y')

# Hide the axis ticks and spines
for ax in axs.flat:
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

# Show the plot
plt.show()
