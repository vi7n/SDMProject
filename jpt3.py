rows = 5
cols = 5
height = 5

def convert_state_to_coordinate(state):
    asd = state % (rows * cols)
    # Compute the first row of the element
    x,y,z = [ asd % cols, asd // cols, state // (rows * cols) ]
    # x, y = state % cols, state // cols
    return x,y,z

def convert_coordinate_to_state(r,c,h):
    position = h * (rows*cols) + c * cols + r
    return position

neighbour_list = []  

num = 99
max = (rows*cols*height) - 1

x,y,z = convert_state_to_coordinate(num)

if not (x-1) < 0:
    a = convert_coordinate_to_state(x-1,y,z)
    print("x-1",a,"coord:",x-1,y,z)
    if a <= max: 
        neighbour_list.append(a)

if not (x+1) > (cols-1):
    a = convert_coordinate_to_state(x+1,y,z)
    print("x+1",a,"coord:",x+1,y,z)
    if a <= max: 
        neighbour_list.append(a)

if not (y-1) < 0:
    a = convert_coordinate_to_state(x,y-1,z)
    print("y-1",a,"coord:",x,y-1,z)
    if a <= max: 
        neighbour_list.append(a)

if not (y+1) > (rows-1):
    a = convert_coordinate_to_state(x,y+1,z)
    print("y+1",a,"coord:",x,y+1,z)
    if a <= max:  
        neighbour_list.append(a)

if not (z-1) < 0:
    a = convert_coordinate_to_state(x,y,z-1)
    print("z-1",a,"coord:",x,y,z-1)
    if a <= max: 
        neighbour_list.append(a)

if not (z+1) > (height-1):
    a = convert_coordinate_to_state(x,y,z+1)
    print("z+1",a,"coord:",x,y,z+1)
    if a <= max: 
        neighbour_list.append(a)

print(neighbour_list)