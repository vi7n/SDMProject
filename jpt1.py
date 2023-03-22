import itertools

# define matrix size
rows = 4
columns = 3
height = 2

# create list of all coordinates in the matrix
coordinates = list(itertools.product(range(rows), range(columns), range(height)))

print(coordinates)
