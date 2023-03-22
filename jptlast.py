import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

global start_state, k_m, open_list, all_state_data


cols = 80
rows = 80
height = 80

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


def convert_state_to_coordinate(state):
    asd = state % (rows * cols)
    # Compute the first row of the element
    x,y,z = [ asd % cols, asd // cols, state // (rows * cols) ]
    # x, y = state % cols, state // cols
    return x,y,z


def convert_coordinate_to_state(r,c,h):
    position = h * (rows*cols) + c * cols + r
    return position


action_steps = []
action_states = []

goal_state = 0
start_state = convert_coordinate_to_state(63,20,70)


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
        # print("utop",u,"utopkey",utopkey())
    
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


obstacles = [(32, 10, 70), (32, 10, 71), (33, 7, 72), (33, 8, 71), (33, 8, 72), (33, 9, 71), (33, 9, 72), (33, 10, 70), (33, 10, 71), (33, 10, 72), (33, 10, 73), (34, 7, 72), (34, 8, 72), (34, 10, 69), (34, 10, 70), (34, 10, 71), (35, 10, 69), (35, 10, 70), (36, 10, 68), (36, 10, 69), (36, 10, 70), (36, 10, 71), (36, 11, 69), (36, 11, 70), (36, 11, 71), (36, 11, 72), (37, 9,54), (37, 9, 57), (37, 9, 58), (37, 9, 69), (37, 10, 54), (37, 10, 57), (37, 10, 58), (37, 10, 61), (37, 10, 62), (37, 10, 68), (37, 10, 69), (37, 11, 68), (37, 11, 69), (37, 11, 71), (37, 11, 72), (38, 9, 54), (38, 9, 57), (38, 9, 58), (38, 9, 61), (38, 9, 63), (38, 9, 64), (38, 9, 65), (38, 9, 66), (38, 9, 67), (38, 9, 69), (38, 9, 70), (38, 9, 71), (38, 9, 72), (38, 10, 54), (38, 10, 55), (38, 10, 56), (38, 10, 57), (38, 10, 58), (38, 10, 59), (38, 10, 60), (38, 10, 61), (38, 10, 62), (38, 10, 63), (38, 10, 64), (38, 10, 65), (38, 10, 66),(38, 10, 67), (38, 10, 68), (38, 10, 69), (38, 10, 70), (38, 10, 71), (38, 10, 72), (38, 11, 50), (38, 11, 56), (38, 11, 59), (38, 11, 60), (38, 11, 61), (38, 11, 62), (38, 11, 67), (38, 11, 68), (39, 9, 64), (39, 9, 65), (39, 9, 72), (39, 9, 73), (39, 10, 50), (39, 10, 51), (39, 10, 55), (39, 10, 56), (39, 10, 57), (39, 10, 58), (39, 10, 59), (39, 10, 61), (39, 10, 62), (39, 10, 63), (39, 10, 64), (39, 10, 65), (39, 10, 66), (39, 10, 67), (39, 10, 68), (39, 10, 69), (39, 10, 70), (39, 10, 71), (39, 11, 49), (39, 11, 50), (39, 11, 51), (39, 11, 54), (39, 11, 55), (39, 11, 56), (39, 11, 57), (39, 11, 58), (39, 11, 59), (39, 11, 60), (39, 11, 61), (39, 11, 62), (39, 11, 63), (39, 11, 64), (39, 11, 65), (39, 11, 66), (39, 11, 67), (39, 11, 68), (39, 11, 69), (39, 11, 70), (39, 12, 59), (40, 7, 66), (40, 7, 67), (40, 8, 55), (40, 8, 65), (40, 8, 66), (40, 8, 67), (40, 9, 49), (40, 9, 50), (40, 9, 51), (40, 9, 55), (40, 9, 56), (40, 9, 57), (40, 9, 58), (40, 9, 60), (40, 9, 61), (40, 9, 62), (40, 9, 63), (40, 9, 65), (40, 9, 66), (40, 10, 49), (40, 10, 50), (40, 10, 51), (40, 10, 52), (40, 10, 53), (40, 10, 54), (40, 10, 55), (40, 10, 56), (40, 10, 57), (40, 10, 58), (40, 10, 59), (40, 10, 60), (40, 10, 61), (40, 10, 62), (40, 10, 63), (40, 10, 64), (40, 10, 65), (40, 10, 66), (40, 10, 67), (40, 10, 68), (40, 10, 70), (40, 10, 71), (40, 11, 48), (40, 11, 49), (40, 11, 50), (40, 11, 51), (40, 11, 52), (40, 11, 53), (40, 11, 54), (40, 11, 55), (40, 11, 56), (40, 11, 57), (40, 11, 58), (40, 11, 59), (40, 11, 60), (40, 11, 61), (40, 11, 62), (40, 11, 63), (40, 11, 64), (40, 11, 65), (40, 11, 66), (40, 11, 67), (40, 11, 68), (40, 11, 69), (40, 11, 70), (40, 12, 55), (40, 12, 56), (40, 12, 57), (40, 12, 58), (40, 12, 59), (40, 12, 60), (40, 13, 53), (40, 13, 54), (40, 13, 55), (40, 13, 56), (40, 14, 66), (41, 8, 51), (41, 8, 54), (41, 8, 55), (41, 8, 65), (41, 9, 48), (41, 9, 49), (41, 9, 50), (41, 9, 51), (41, 9, 52), (41, 9, 53), (41, 9, 54), (41, 9, 55), (41, 9, 56), (41, 9, 57), (41, 9, 58), (41, 9, 59), (41, 9, 60), (41, 9, 61), (41, 9, 62), (41, 9, 63), (41, 9, 65), (41, 9, 66), (41, 9, 67), (41, 9, 68), (41, 10, 49), (41, 10, 50), (41, 10, 51), (41, 10, 52), (41, 10, 53), (41, 10, 54), (41, 10, 55), (41, 10, 56), (41, 10, 57), (41, 10, 58), (41, 10, 59), (41, 10, 60), (41, 10, 61), (41, 10, 62), (41, 10, 63), (41, 10, 64), (41, 10, 65), (41, 10, 66), (41, 10, 67), (41, 10, 68), (41, 10, 69), (41, 10, 70), (41, 10, 71), (41, 11, 49), (41, 11, 58), (41, 11, 59), (41, 11, 60), (41, 11, 63), (41, 11, 64), (41, 11, 65), (41, 11, 68), (41, 11, 69), (41, 11, 70), (41, 12, 51), (41, 12, 52), (41, 12, 53), (41, 12, 54), (41, 12, 55), (41, 12, 58), (41, 13, 53), (41, 13, 54), (41, 13, 55), (42, 9, 50), (42, 9, 51), (42, 9, 60), (42, 10, 50), (42, 10, 51), (42, 10, 59), (42, 10, 60), (42, 10, 61), (42, 10, 63), (42, 10, 64), (42, 10, 65), (42, 11, 49), (42, 11, 50), (42, 11, 51), (42, 11, 52), (42, 11, 59), (42, 11, 60), (42, 11, 64), (42, 11, 65), (42, 12, 50), (42, 12, 51), (42, 12, 52), (42, 12, 53), (43, 0, 64), (43, 1, 64), (43, 10, 49), (43, 10, 50), (43, 10, 59), (43, 10, 60), (43, 10, 61), (43, 10, 64), (43, 10, 65), (43, 11, 49), (43, 11, 50), (43, 11, 51), (43, 11, 59), (43, 11, 60), (43, 11, 64), (43, 11, 65), (43, 12, 50), (44, 0, 64), (44, 9, 61), (44, 9, 62), (44, 10, 50), (44, 10, 60), (44, 10, 61), (44, 10, 62), (44, 11, 49), (44, 11, 50), (44, 11, 60), (44, 11, 61), (44, 12, 51), (45, 0, 64), (45, 8, 63), (45, 9, 61), (45, 9, 62), (45, 9, 63), (45, 10, 50), (45, 10, 61), (45, 10, 62), (45, 11, 50), (45, 11, 51), (45, 11, 60), (45, 11, 61), (45, 12, 50), (45, 12, 51), (45, 48, 43), (45, 74, 65), (45, 74, 66), (45, 75, 65), (45, 75, 66), (45, 76, 65), (45, 76, 66), (45, 77, 65), (46, 0, 63), (46, 0, 64), (46, 0, 65), (46, 1, 63), (46, 1, 64), (46, 2, 63), (46, 2, 64), (46, 3, 62), (46, 3, 63), (46, 4, 62), (46, 4, 63), (46, 5, 62), (46, 5, 63), (46, 6, 62), (46, 7, 62), (46, 10, 50), (46, 10, 51), (46, 10, 61), (46, 11, 50), (46, 11, 51), (46, 11, 60), (46, 11, 61), (46, 12, 50), (46, 12, 51), (46, 74, 66), (46, 75, 66), (46, 76, 65), (46, 76, 66), (46, 77, 64), (46, 77, 65), (46, 78, 64), (46, 78, 65), (46, 79, 64), (46, 79, 65), (47, 0, 64), (47, 0, 65), (47, 0, 66), (47, 0, 67), (47, 0, 68), (47, 1, 64), (47, 2, 63), (47, 2, 64), (47, 3, 63), (47, 4, 63), (47, 5, 62), (47, 5, 63), (47, 6, 62), (47, 6, 63), (47, 7, 61), (47, 7, 62), (47, 8, 61), (47, 8, 62), (47, 9, 61), (47, 9, 62), (47, 10, 50), (47, 10, 51), (47, 10, 61), (47, 10, 62), (47, 10, 63), (47, 10, 64), (47, 10, 65), (47, 10, 66), (47, 10, 67), (47, 10, 68), (47, 11, 50), (47, 11, 51), (47, 11, 60), (47, 11, 61), (47, 11, 62), (47, 11, 63), (47, 11, 64), (47, 11, 65), (47, 11, 66), (47, 11, 67), (48, 0, 67), (48, 0, 68), (48, 9, 51), (48, 10, 51), (48, 10, 61), (48, 10, 67), (48, 10, 68), (48, 11, 50), (48, 11, 51), (48, 11, 60), (48, 11, 61), (48, 11, 62), (48, 11, 63), (48, 11, 64), (48, 11, 65), (48, 11, 66), (48, 11, 67), (48, 11, 68), (49, 9, 51), (49, 9, 52), (49, 10, 51), (49, 10, 52), (49, 10, 61), (49, 11, 61), (50, 9, 51), (50, 9, 52), (50, 10, 51), (50, 10, 52), (51, 8, 54), (51, 8, 55), (63, 19, 69), (62, 19, 69), (62, 19, 68), (62, 18, 68), (61, 18, 68), (61, 18, 67), (61, 17, 67), (60, 17, 67), (60, 17, 66), (60, 16, 66), (59, 16, 66), (59, 16, 65), (59, 15, 65), (58, 15, 65), (58, 15, 64), (58, 14, 64), (57, 14, 64), (57, 14, 63), (57, 13, 63), (56, 13, 63), (56, 13, 62), (56, 12, 62), (55, 12, 62), (55, 12, 61), (55, 11, 61), (54, 11, 61), (54, 11, 60), (54, 10, 60), (53, 10, 60), (53, 10, 59), (53, 9, 59), (52, 9, 59), (52, 9, 58), (52, 8, 58), (51, 8, 58), (51, 8, 57), (51, 7, 57), (50, 7, 57), (50, 7, 56), (50, 6, 56), (49, 6, 56), (49, 6, 55), (49, 5, 55), (24, 0, 31), (24, 0, 30), (23, 0, 30), (23, 0, 29), (22, 0, 29), (22, 0, 28), (21, 0, 28), (21, 0, 27), (20, 0, 27), (20, 0, 26), (19, 0, 26), (19, 0, 25), (18, 0, 25), (18, 0, 24), (17, 0, 24), (17, 0, 23), (16, 0, 23), (16, 0, 22), (15, 0, 22), (15, 0, 21), (14, 0, 21), (14, 0, 20), (13, 0, 20), (13, 0, 19), (12, 0, 19), (12, 0, 18), (11, 0, 18), (11, 0, 17), (10, 0, 17), (10, 0, 16), (9, 0, 16), (9, 0, 15), (8, 0, 15), (8, 0, 14), (7, 0, 14), (7, 0, 13), (6, 0, 13), (6, 0, 12)]


block_list = obstacles
circle_list = action_steps

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





