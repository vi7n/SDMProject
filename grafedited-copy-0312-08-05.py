import numpy as np
import matplotlib.pyplot as plt

global start_state, k_m, open_list, all_state_data


cols = 5
rows = 4
number_of_states = rows * cols


goal_state = 0
start_state = 19


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
open_list.append(all_state_data[goal_state])

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


# takes the co-ordinate and updates the elemnt's g and rhs value in the all state data i.e. the grid
# def update_g_rhs(s):
#     x, y = s
#     state = convert_coordinate_to_state(x,y)
#     all_state_data[state][1] = CalculateKey(s)
#     return
    # calculate key uses the all state list or the open list?


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
    # print("sssssssssssssssssssssssssss",s)
    # function checked. works correctly
    if s != None:
        # print("yo ho hai____",s)
        if s == [np.inf, np.inf]: #this if was added to fix non-iterable error but it might not be required anymore 
            print("line 112 error:::::::::::::::::::::::::::::::::")
            return tuple(s)

        g,rhs = s[1]
        # print(g,rhs)

        b = min(g,rhs) 
        a = b + heuristic(all_state_data[start_state],s) + k_m
        # print("##########################################",all_state_data[start_state])
        # print("##########################################",a,b)
        return(a,b)


# takes the state as input updates the vertex
def updatevertex(u):
    g_u, rhs_u = all_state_data[u][1]
    # print (g_u,rhs_u) 

    if ( (g_u != rhs_u ) and isthisinopenlist(convert_state_to_coordinate(u))):
        # U.update(u,CalculateKey(u))
        aaa = CalculateKey((convert_state_to_coordinate(u),all_state_data[u][1]))
        u_update(convert_state_to_coordinate(u),aaa)
        # all_state_data[u][1][0] =  all_state_data[u][1][1]

    elif ( (g_u != rhs_u ) and not isthisinopenlist(convert_state_to_coordinate(u))):
        open_list.append((convert_state_to_coordinate(u),CalculateKey((convert_state_to_coordinate(u),all_state_data[u][1]))))

    elif ( (g_u == rhs_u) and isthisinopenlist(convert_state_to_coordinate(u)) ) :
        remove_element(convert_state_to_coordinate(u))

    return


    # s_x, s_y = convert_state_to_coordinate(s)
    # if (s != 0):
    #     succ = pred(s)
    #     min_val = np.inf
    #     for element_state in succ:
    #         element = (element_state % cols, element_state//cols)
    #         # print("element:",element)
    #         if min_val > get_g_and_rhs(element)[0]:
    #             min_val = get_g_and_rhs(element)[0]  
    #             # print("min_val:",min_val)
    #     all_state_data[s][1][1] = 1 + min_val
    # if isthisinopenlist((s_x,s_y)):
    #     remove_element((s_x,s_y))
    # g, rhs = get_g_and_rhs((s_x,s_y))
    # if (g != rhs):
    #     open_list.append([(s_x,s_y),(g,rhs)])



        # print("Append open l;ist", open_list)
        # update_g_rhs(s)
    # elif (g != rhs) and not isthisinopenlist(s[0]):
    #     open_list.append(s)
    # elif (g == rhs) and isthisinopenlist(s[0]):
    #     remove_element(s)


# define hweristic here, currently returns zero
# takes the entire state as input
def heuristic(p,q):
    # function checked. works correctly
    # print("-------------------------------------------------",p[0],q[0])
    
    x1, y1 = p[0]

    x2, y2 = q[0]

    # taking the euclidean as the heuristic
    h = ((abs(x2-x1))**2+(abs(y2-y1)**2)**(1/2))
    # print("heuristic:",h)
    
    # return h
    return 0


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
    # print(sorted_elements)
    # print(sorted_elements[0])
    return sorted_elements[0]



    # global open_list
    # if isopenlistempty():
    #     return[np.inf,np.inf]
    # sum_list = [] 

    # for element in open_list:
    #     if np.inf in element[1]:
    #         continue
    #     else:
    #         sum_list.append((element, np.sum(element[1])))

    # # Sort the list of elements by their sum
    # open_list = sorted(open_list, key=lambda x: x[1])
    # print("sum_list:",sum_list)
    # # If there are no elements with finite sum, return None
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
    # return open_list[0]
    

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


# g and rhs data type is float
# g, rhs = np.inf , np.inf
# state = all_state_data[0]
# print(state)


# takes the co-ordinates and returns true if g > rhs
def gu_greater_than_rhsu(x,y):
    state = convert_coordinate_to_state(x,y)
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


# takes in 2 states and returns the cost
def cost(a,b):
    x1,y1 = convert_state_to_coordinate(a)
    x2,y2 = convert_state_to_coordinate(b)

    # check if obstalce and calc cost
    # 
    return 1 


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
        # print("::::::::::::::::::::::",utopkey(),CalculateKey(all_state_data[start_state]))
        u = utop()
        k_old = utopkey()
        k_new = CalculateKey(u)

        # print(k_new)
        # print("**********************************",u, u[0])
        xx , yy = u[0]
        state = convert_coordinate_to_state(xx,yy)
        # print(state,xx,yy)
        # g_u, rhs_u = u[1]

        if k_old < k_new :
            u_update(u[0],k_new)
            # print("yo na hunu parne")

        elif gu_greater_than_rhsu(xx, yy): #g(u) > rhs(u)
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

        print("openlis:",open_list)
        print("utop",u,"utopkey",utopkey())
    
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

    
    
    return





    







    # goal = 19
    # start_state = 19

    # ut = utopkey() 
    # # print("---------------",ut)
    # calkey = CalculateKey(all_state_data[start_state])
    # # print("---------------",)
    # # print("---------------",calkey)
    # rhs_s_start = all_state_data[start_state][1][1]
    # g_s_start = all_state_data[start_state][1][0]  

    # if ut == None:
    #     ut = 0
    # # print(ut,calkey[0],calkey[1])

    # if calkey[0] == np.inf and calkey[1] == np.inf:
    #     flag = True

    
    # while ( (ut <= calkey) or ( all_state_data[start_state][1][1] != all_state_data[start_state][1][0]  ) ):
        
    #     print("open list", open_list, "state_val", all_state_data[start_state][1], "ut", (ut, calkey))
       
    #     u = utop()
      
    #     print("popped", u)

    #     k_old = utopkey()
    #     remove_element(u[0])
    #     # print(k_old)
    #     k_new = CalculateKey(u)
    #     # input("press enter to continue")
    #     # print(k_new, k_old)
    #     print("k vako ho yoooooooooooooooooooo",u[0])
    #     x, y = u[0]
    #     state = convert_coordinate_to_state(x,y)
    #     if k_old < k_new :
    #         u_update(u,k_new)

    #     elif gu_greater_than_rhsu(u[0]):
            
    #         # g,rhs = all_state_data[state][1]
    #         all_state_data[state][1][0] = all_state_data[state][1][1]   #g(u) = rhs(u)
            
    #         results = pred(state)
    #         # print("results", results)
    #         for result in results:
    #             updatevertex(result)
    #         # print("UPDAREDS", open_list)
    #     else:
    #         all_state_data[state][1][0] = np.inf
    #         updatevertex(state)
    #         succ = pred(state)
    #         for element_state in succ:
    #             updatevertex(element_state)
    #     ut = utopkey() 
    #     calkey = CalculateKey(all_state_data[start_state])

    #     print("open list", open_list, "state_val", all_state_data[start_state][1], "ut", (ut, calkey))

last_state = start_state
computeshortestpath()

# while (start_state != goal_state):
#     if all_state_data[start_state][1][1] == np.inf :
#         print("THERE IS NO KNOWN PATH")
#     start_state = argmin_succ(start_state)

    # move to S_start
    # scan graph for changed edges cost
    # if any_cost_changed():
    #     k_m = k_m + heuristic(last_state,start_state)
    #     last_state = start_state














            











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