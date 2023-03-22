# same as last onle but added convert functions




import numpy as np
import matplotlib.pyplot as plt

global start_state, k_m, open_list, all_state_data


cols = 5
rows = 8
number_of_states = rows * cols


goal_state = 0
start_state = 39


# initialize() part 1 as per the D* Lite (Optimized version)
k_m = 0
open_list = []

all_state_data = []

# loop to initialize all_state_data
for i in range(number_of_states):
    # Compute the first row of the element
    first_row = [i % cols, i // cols]
    # Create the matrix
    element = [first_row, [np.inf, np.inf]]
    # Add the element to the list
    all_state_data.append(element)
    # each element is a 2*2 array: [[x_co-ordinate,y_co-ordinate],[g,rhs]]

# set the rhs value of goal state to 0, making goal state inconsistent
all_state_data[goal_state][1][1] = 0 

# add the goal in open list
open_list.append([[0,0],[0,0]])

# initialize part 1 end ///\\\


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
    x, y = state % cols, state // cols
    return x,y

def convert_coordinate_to_state(r,c):
    position = c * cols + r
    return position



# takes the co-ordinate and updates the elemnt's g and rhs value 
def update_g_rhs(s):
    x, y = s
    state = convert_coordinate_to_state(x,y)
    all_state_data[state][1] = CalculateKey(s)





def updatevertex(s):
    s_x, s_y =  s % cols, s // cols
    if (s != 0):
        succ = pred(s)
        min_val = np.inf
        for element_state in succ:
            element = (element_state % cols, element_state//cols)
            # print("element:",element)
            if min_val > get_g_and_rhs(element)[0]:
                min_val = get_g_and_rhs(element)[0]  
                # print("min_val:",min_val)
        all_state_data[s][1][1] = 1 + min_val
    if isthisinopenlist((s_x,s_y)):
        remove_element((s_x,s_y))
    g, rhs = get_g_and_rhs((s_x,s_y))
    if (g != rhs):
        open_list.append([(s_x,s_y),(g,rhs)])
        # print("Append open l;ist", open_list)
        # update_g_rhs(s)
    # elif (g != rhs) and not isthisinopenlist(s[0]):
    #     open_list.append(s)
    # elif (g == rhs) and isthisinopenlist(s[0]):
    #     remove_element(s)


def heuristic(p,q):
    # function checked. works correctly
    print("-------------------------------------------------",p,q)
    x1, y1 = p[0]
    x2, y2 = q[0]

    # taking the euclidean as the heuristic
    h = ((abs(x2-x1))**2+(abs(y2-y1)**2)**(1/2))
    # print("heuristic:",h)
    
    # return h
    return 0



def CalculateKey(s):
    # function checked. works correctly
    if s != None:
        print("yo ho hai____",s)
        if s == [np.inf, np.inf]: #this if was added to fix non-iterable error but it might not be required anymore 
            print("lamooooooooooooooooooooooooooooooooooooooooooooooooooo")
            return tuple(s)


        g,rhs = s[1]
        # print(g,rhs)

        b = min(g,rhs) 
        a = b + heuristic(all_state_data[start_state],s) + k_m
        print("##########################################",all_state_data[start_state])

        return(a,b)


def utop():
    global open_list
    if isopenlistempty():
        return[np.inf,np.inf]
    # sum_list = [] 

    # for element in open_list:
    #     if np.inf in element[1]:
    #         continue
    #     else:
    #         sum_list.append((element, np.sum(element[1])))

    # Sort the list of elements by their sum
    open_list = sorted(open_list)#, key=lambda x: x[1])
    # print("sum_list:",sum_list)
    # If there are no elements with finite sum, return None
    # if not sum_list:
    #     result = None
    # else:
    #     # Get the element with the least sum
    #     min_sum = sum_list[0][1]
    #     min_sum_list = [x for x in sum_list if x[1] == min_sum]
    #     # If there are multiple elements with the least sum, randomly select one
    #     # print(min_sum_list)
    #     result = min_sum_list[0][0]#np.random.choice(min_sum_list)[0]
    #     # print("results", result)
    return open_list[0]
    

def utopkey():
    s = utop()

    if s == [np.inf, np.inf]:
        print("end of list")
        return tuple([np.inf,np.inf])

    elif s != None:
        print("---------",s)
        print("openlist:",open_list)
        return tuple(s[1])
    
    return None





# g and rhs data type is float
# g, rhs = np.inf , np.inf
# state = all_state_data[0]
# print(state)


def u_update(u,k):
    for i in range(len(open_list)):
        if np.array_equal(open_list[i][0], u[0]):
            # Replace the element with the new one
            open_list[i][1] = k
            return
    print("ye kya hogaya")
    return

# only take s[0]
def get_g_and_rhs(s):
    x, y = s
    state = convert_coordinate_to_state(x,y)
    dat = all_state_data[state][1]
    # print("returned g and rhs from vertex data:", dat)
    return dat


def gu_greater_than_rhsu(u):
    g,rhs = get_g_and_rhs(u[0]) 
    if g > rhs:
        return True
    # elif g == rhs:
    #     print("duitai barabar")
    # else:
    #     print("ye kya huwa?")
    return False


def pred(num):
    numbers = []
    rem = num % cols
    if num + cols < number_of_states:
        numbers.append(num + cols)
    if num - cols >= 0:
        numbers.append(num - cols)
    if num - 1 >= 0 and rem != 0:
        numbers.append(num - 1)
    if num + 1 < number_of_states and rem != (cols - 1):
        numbers.append(num + 1)
    return numbers



def computeshortestpath():
    # goal = 19
    # start_state = 19

    ut = utopkey() 
    # print("---------------",ut)
    calkey = CalculateKey(all_state_data[start_state])
    # print("---------------",)
    # print("---------------",calkey)
    rhs_s_start = all_state_data[start_state][1][1]
    g_s_start = all_state_data[start_state][1][0]  

    if ut == None:
        ut = 0
    # print(ut,calkey[0],calkey[1])

    if calkey[0] == np.inf and calkey[1] == np.inf:
        flag = True

    
    while ( (ut <= calkey) or ( all_state_data[start_state][1][1] != all_state_data[start_state][1][0]  ) ):
        
        print("open list", open_list, "state_val", all_state_data[start_state][1], "ut", (ut, calkey))
       
        u = utop()
      
        print("popped", u)

        k_old = utopkey()
        remove_element(u[0])
        # print(k_old)
        k_new = CalculateKey(u)
        # input("press enter to continue")
        # print(k_new, k_old)
        print("k vako ho yoooooooooooooooooooo",u[0])
        x, y = u[0]
        state = convert_coordinate_to_state(x,y)
        if k_old < k_new :
            u_update(u,k_new)

        elif gu_greater_than_rhsu(u):
            
            # g,rhs = all_state_data[state][1]
            all_state_data[state][1][0] = all_state_data[state][1][1]   #g(u) = rhs(u)
            
            results = pred(state)
            # print("results", results)
            for result in results:
                updatevertex(result)
            # print("UPDAREDS", open_list)
        else:
            all_state_data[state][1][0] = np.inf
            updatevertex(state)
            succ = pred(state)
            for element_state in succ:
                updatevertex(element_state)
        ut = utopkey() 
        calkey = CalculateKey(all_state_data[start_state])

        print("open list", open_list, "state_val", all_state_data[start_state][1], "ut", (ut, calkey))

computeshortestpath()








            











# print("the curent state is:",state[0])
# print("the current g, rhs is:",state[1,0],state[1,1])


# # Code to edit the state values
# inp = int(input("Do you want to change it? (yes = 1)"))
# # print(type(inp))
# if inp == 1:
#     # print("bhitra")
#     state[0,0] = input("x_co-ordinate:")
#     state[0,1] = input("y_co-ordinate:")
#     state[1,0] = input("g?")
#     num = input("rhs?")
#     if num == np.inf:
#         print("infinity chalyo hai")
#         state[1,1] = np.inf


#  s data type is list, 
# s = [g,rhs]

# print(CalculateKey(state))

# print(s,type(s),type(g),type(rhs))

# print (isopenlistempty())

# open_list.append([[1, 2],[np.inf,np.inf]])

# print(isopenlistempty())
# print(isthisinopenlist([1,2]))

# open_list.remove([1, 2])

# print(isopenlistempty())
# print(isthisinopenlist([1,2]))

fig, axs = plt.subplots(nrows=rows, ncols=cols)

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