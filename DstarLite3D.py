import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

global start_state, k_m, open_list, all_state_data


cols = 20
rows = 20
height = 20

number_of_states = rows * cols * height

costi = np.ones((cols,rows,height))
costi[2][2][2] = 100000

def generate_obstacles(n, rows, cols, height):
    coordinates = []
    for i in range(n):
        x = random.randint(0, rows-1)
        y = random.randint(0, cols-1)
        z = random.randint(0, height-1)
        coordinates.append((x, y, z))
        costi[x][y][z] = 10000 

    return coordinates

# Example usage: generate 5 random coordinates in a 3x4x5 cube
number_of_obstacles = 20
n = number_of_obstacles
# p = 3
# q = 4
# r = 5
obstacles = []
obstacles = generate_obstacles(n, rows, cols, height)
lamo = [(19, 19, 18), (19, 18, 18), (18, 18, 18), (18, 18, 17), (18, 17, 17), (17, 17, 17), (17, 17, 16), (17, 16, 16), (16, 16, 16), (16, 16, 15), (16, 15, 15), (15, 15, 15), (15, 15, 14), (15, 14, 14), (14, 14, 14), (14, 14, 13), (14, 13, 13), (13, 13, 13), (13, 13, 12), (13, 12, 12), (12, 12, 12), (12, 12, 11), (12, 11, 11), (11, 11, 11), (11, 11, 10), (11, 10, 10), (10, 10, 10), (10, 10, 9), (10, 9, 9), (9, 9, 9), (9, 9, 8), (9, 8, 8), (8, 8, 8), (8, 8, 7), (8, 7, 7), (7, 7, 7), (7, 7, 6), (7, 6, 6), (6, 6, 6), (6, 6, 5), (6, 5, 5), (5, 5, 5), (5, 5, 4), (5, 4, 4), (4, 4, 4), (4, 4, 3), (4, 3, 3), (3, 3, 3), (3, 3, 2), (3, 2, 2), (3, 2, 1), (2, 2, 1), (2, 1, 1), (1, 1, 1), (1, 1, 0), (1, 0, 0), (0, 0, 0)]
for element in lamo:
    obstacles.append(element)
# print(coordinates)





action_steps = []
action_states = []

goal_state = 0
start_state = (rows*cols*height)-1


# initialize() part 1 as per the D* Lite (Optimized version)
k_m = 0
open_list = []

all_state_data = []

# loop to initialize all_state_data
for i in range(number_of_states):
    asd = i % (rows * cols)
    # Compute the first row of the element
    first_row = [ asd % cols, asd // cols, i // (rows * cols) ]
    # Create the matrix
    element = [first_row, [np.inf, np.inf]]
    # Add the element to the list
    all_state_data.append(element)
    # each element is a 2*2 array: [[x_co-ordinate,y_co-ordinate],[g,rhs]]

# set the rhs value of goal state to 0, making goal state inconsistent
all_state_data[goal_state][1][1] = 0 


# add the goal in open list
open_list.append(all_state_data[goal_state])

# initialize part 1 end ///\\\

# print(all_state_data)


# function to check if the open list is empty
def isopenlistempty():
    if not open_list:
        a = True
    else:
        a = False
    return a
    

# takes the co-ordinate and returns if it is in open list
def isthisinopenlist(s):
    a = False
    if not isopenlistempty():
        for element in open_list:
            if element[0] == s:
                a = True   
    return a


# takes the co-ordinate and removes it from the openlist
def remove_element(s):
    # print(s)
    # might have to check if list is empty
    for element in open_list:
        if element[0] == s:
            open_list.remove(element)
            
            # print("element:",element,"removed")
            return
    # print(s)
    if isopenlistempty():
        print("this is remove_element function. LIST IS EMPTY!")
    print("No element found??????????")
    return


def convert_state_to_coordinate(state):
    asd = state % (rows * cols)
    # Compute the first row of the element
    x,y,z = [ asd % cols, asd // cols, state // (rows * cols) ]
    # x, y = state % cols, state // cols
    return x,y,z


def convert_coordinate_to_state(r,c,h):
    position = h * (rows*cols) + c * cols + r
    return position



#  takes: co-ordinate and priority. Does: updates the priority in the open list
def u_update(u,k):
    # print("90909090",u,k)

    for element in open_list:
        if element[0] == u:
            remove_element(u)
            open_list.append((u,k))
            return
    print("ye kya hogaya")
    return


# takes the ENTIRE ELEMENT ([co-ordinate],[priority]) returns the priority
def CalculateKey(s):
    if s != None:
        if s == [np.inf, np.inf]: #this if was added to fix non-iterable error but it might not be required anymore 
            print("line 112 error:::::::::::::::::::::::::::::::::")
            return tuple(s)

        g,rhs = s[1]
        # print(g,rhs)

        b = min(g,rhs) 
        a = b + heuristic(all_state_data[start_state],s) + k_m
        return(a,b)


# takes the state as input updates the vertex
def updatevertex(u):
    g_u, rhs_u = all_state_data[u][1]
    # print (g_u,rhs_u) 

    if ((g_u != rhs_u ) and isthisinopenlist(convert_state_to_coordinate(u))):
        # U.update(u,CalculateKey(u))
        aaa = CalculateKey((convert_state_to_coordinate(u),all_state_data[u][1]))
        u_update(convert_state_to_coordinate(u),aaa)
        # all_state_data[u][1][0] =  all_state_data[u][1][1]

    elif ( (g_u != rhs_u ) and not isthisinopenlist(convert_state_to_coordinate(u))):
        open_list.append((convert_state_to_coordinate(u),CalculateKey((convert_state_to_coordinate(u),all_state_data[u][1]))))

    elif ( (g_u == rhs_u) and isthisinopenlist(convert_state_to_coordinate(u)) ) :
        remove_element(convert_state_to_coordinate(u))

    return


# returns zero right now
def heuristic(p,q):
    # function checked. works correctly
    # print("-------------------------------------------------",p[0],q[0])
    
    x1, y1, z1 = p[0]

    x2, y2, z2 = q[0]

    # taking the euclidean as the heuristic
    h = 50*(((abs(x2-x1))**2+(abs(y2-y1)**2)+(abs(z2-z1))**2)**(1/2))
    # print("heuristic:",h)
    
    # return h
    return h


def sort_key(element):
    second_row = element[1]
    if np.isinf(second_row[0]):
        return (np.inf, second_row[1])
    else:
        return (sum(second_row), second_row[0])


# utop defined in the algo. returns the element with least priority
def utop():
    if isopenlistempty():
        return[np.inf,np.inf]
    sorted_elements = sorted(open_list, key = sort_key)

    return sorted_elements[0]
    

# returns the least priority of open list. if list empty returns [inf,inf]
def utopkey():
    s = utop()

    if s == [np.inf, np.inf]:
        print("end of list")
        return tuple([np.inf,np.inf])

    elif s != None:
        # print("---------",s,"=====",s[1])
        # print("openlist:",open_list)
        return tuple(s[1])
    
    return None


# takes the co-ordinates and returns true if g > rhs
def gu_greater_than_rhsu(x,y,z):
    state = convert_coordinate_to_state(x,y,z)
    g,rhs = all_state_data[state][1]
    # print(g,rhs)
    if g > rhs:
        return True
    # elif g == rhs:
    #     print("duitai barabar")
    else:
        # print("ye kya huwa?")
        return False


# takes the state and return state of all predessors
def pred(num):
    neighbour_list = []    
    x,y,z = convert_state_to_coordinate(num)

    if not (x-1) < 0:
        a = convert_coordinate_to_state(x-1,y,z)
        # print("x-1",a,"coord:",x-1,y,z)
        if a < number_of_states:
            neighbour_list.append(a)

    if not (x+1) >= cols:
        a = convert_coordinate_to_state(x+1,y,z)
        # print("x+1",a,"coord:",x+1,y,z)
        if a < number_of_states:
            neighbour_list.append(a)

    if not (y-1) < 0:
        a = convert_coordinate_to_state(x,y-1,z)
        # print("y-1",a,"coord:",x,y-1,z)
        if a < number_of_states:
            neighbour_list.append(a)

    if not (y+1) >= rows:
        a = convert_coordinate_to_state(x,y+1,z)
        # print("y+1",a,"coord:",x,y+1,z)
        if a < number_of_states:
            neighbour_list.append(a)

    if not (z-1) < 0:
        a = convert_coordinate_to_state(x,y,z-1)
        # print("z-1",a,"coord:",x,y,z-1)
        if a < number_of_states:
            neighbour_list.append(a)

    if not (z+1) >= height:
        a = convert_coordinate_to_state(x,y,z+1)
        # print("z+1",a,"coord:",x,y,z+1)
        if a < number_of_states:
            neighbour_list.append(a)

    return neighbour_list


costi = np.ones((cols,rows,height))
costi[2][2][2] = 100000

# takes in 2 states and returns the cost
def cost(a,b):
    x1,y1,z1 = convert_state_to_coordinate(a)
    x2,y2,z2 = convert_state_to_coordinate(b)

    a = costi[x2][y2][z2]

    if a != 1:
        return 10000
    
    else:
        return 1

    # check if obstalce and calc cost
    # 
    # return a


#takes in a state, returns minimum (cost + neighbour g)
def minimum_c_plus_g(state):
    val = []
    results = pred(state)
    for result in results:
        a = cost(state,result) + all_state_data[result][1][0]
        val.append(a)

    sorti = sorted(val)
    return sorti[0]


# takes in a state, returns the neighbour with minimum (cost + g)
def argmin_succ(state):
    val = []
    results = pred(state)
    for result in results:
        a = cost(state,result) + all_state_data[result][1][0]
        val.append([result,a])

    sorti = sorted(val, key=lambda x: x[1])
    return sorti[0][0]


# as the name suggets:
def computeshortestpath():

    g_start, rhs_start = all_state_data[start_state][1]
    # print(g_start,rhs_start)

    while ( (utopkey() <= CalculateKey(all_state_data[start_state])) or ( rhs_start > g_start) ):
        u = utop()
        k_old = utopkey()
        k_new = CalculateKey(u)

        xx , yy , zz = u[0]
        state = convert_coordinate_to_state(xx,yy,zz)
        
        if k_old < k_new :
            u_update(u[0],k_new)
            # print("yo na hunu parne")

        elif gu_greater_than_rhsu(xx, yy,zz): #g(u) > rhs(u)
            all_state_data[state][1][0] = all_state_data[state][1][1]  #g(u) = rhs(u)
            remove_element(u[0])
            results = pred(state)
            # print("results", results)
            for result in results:
                if result != goal_state:
                    
                    min_a = all_state_data[result][1][1]
                    min_b = cost(result,state) + all_state_data[state][1][0]
                    all_state_data[result][1][1] = min(min_a, min_b)
                    updatevertex(result)
        else:
            g_old = all_state_data[state][1][0]
            all_state_data[state][1][0] = np.inf
            results = pred(state)
            result.append(state)
            for result in results:
                if all_state_data[result][1][1] == (cost(result,u) + g_old):
                    if result != goal_state:
                        all_state_data[result][1][1] = minimum_c_plus_g(result)
                    updatevertex(result)

        # print("openlis:",open_list)
        print("utop",u,"utopkey",utopkey())
    
    # fig, axs = plt.subplots(nrows=rows, ncols=cols)

    # for i, element in enumerate(all_state_data):
    #     # Get the x and y coordinates from the first row of the element
    #     x, y = element[0]
    #     # Get the value to show in the cell from the second row of the element
    #     value = element[1]
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

    
    
    return





    



last_state = start_state
computeshortestpath()
# counter = 0
while (start_state != goal_state):
    if all_state_data[start_state][1][1] == np.inf :
        print("THERE IS NO KNOWN PATH")
    # if counter == 0:
    #     costi[0][0][3] =  np.inf
    start_state = argmin_succ(start_state)

    action_steps.append(convert_state_to_coordinate(start_state))
    action_states.append(start_state)
    # counter+=1

print(action_steps)
print(action_states)

    # move to S_start
    # scan graph for changed edges cost
    # if any_cost_changed():
    #     k_m = k_m + heuristic(last_state,start_state)
    #     last_state = start_state

list1 = action_steps
list2 = obstacles

data = np.zeros((rows, cols, height))
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
ax.set_xlim(0, rows)
ax.set_ylim(0, cols)
ax.set_zlim(0, height)

# show the plot
plt.show()





