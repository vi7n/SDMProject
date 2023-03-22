import numpy as np
import matplotlib.pyplot as plt

global s_start, k_m, open_list, all_state_data

number_of_states = 20
goal_position = 0

s_start = np.array([[4, 2], [np.inf, np.inf]])

# initialize()
k_m = 0
open_list = []

all_state_data = []

for i in range(number_of_states):
    # Compute the first row of the element
    first_row = [i % 5, i // 5]
    # Create the matrix
    element = [first_row, [np.inf, np.inf]]
    # Add the element to the list
    all_state_data.append(element)

# goal state is (0,0) thus:
# print("after:",all_state_data)
all_state_data[0][1][1] = 0 
# print("after:",all_state_data)
open_list.append([[0,0],[0,0]])



# initialize end ///\\\



# Print the generated list
# print(all_state_data)



zero_state = np.zeros((2, 2))
# the state is a 2*2 array: [[x_co-ordinate,y_co-ordinate],[g,rhs]]


def isopenlistempty():
    # function checked. works correctly
    if not open_list:
        # print("the list is empty")
        a = True
    else:
        a = False
    return a
    

# only send the co-ordinate i.e. state[0]
def isthisinopenlist(s):
    # function checked. works correctly
    a = False
    if not isopenlistempty():
        for element in open_list:
            if element[0] == s:
            # print("is in open list")
                a = True   
    return a


# only send the co-ordinate i.e. state[0]
def remove_element(s):
    # might have to check if list is empty
    for element in open_list:
        if element[0] == s:
            open_list.remove(element)
            print("element:",element,"removed")
            return
    print("No element found??????????")
    return


def update_g_rhs(s):
    x, y = s[0]
    position = y * 5 + x
    all_state_data[position][1] = CalculateKey(s)





def updatevertex(s):
    g, rhs = get_g_and_rhs(s[0])
    if (g != rhs) and isthisinopenlist(s[0]):
        update_g_rhs(s)
    elif (g != rhs) and not isthisinopenlist(s[0]):
        open_list.append(s)
    elif (g == rhs) and isthisinopenlist(s[0]):
        remove_element(s)


def CalculateKey(s):
    # function checked. works correctly
    if s != None:
        g,rhs = s[1]
        # print(g,rhs)

        b = min(g,rhs) 
        a = b + heuristic(s_start,s) + k_m 

        return(a,b)


def heuristic(p,q):
    # function checked. works correctly
    x1, y1 = p[0]
    x2, y2 = q[0]

    # taking the euclidean as the heuristic
    h = ((abs(x2-x1))**2+(abs(y2-y1)**2)**(1/2))
    # print("heuristic:",h)
    
    # return h
    return 0

def utop():
    if isopenlistempty():
        return[np.inf,np.inf]
    sum_list = []

    for element in open_list:
        if np.inf in element[1]:
            continue
        else:
            sum_list.append((element, np.sum(element[1])))

    # Sort the list of elements by their sum
    sum_list = sorted(sum_list, key=lambda x: x[1])

    # If there are no elements with finite sum, return None
    if not sum_list:
        result = None
    else:
        # Get the element with the least sum
        min_sum = sum_list[0][1]
        min_sum_list = [x for x in sum_list if x[1] == min_sum]
        # If there are multiple elements with the least sum, randomly select one
        result = np.random.choice(min_sum_list[0])

    return(result)

def utopkey():
    s = utop()
    if s != None:
        print(s)
        return s[1]
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
    position = y * 5 + x
    dat = all_state_data[position,1]
    print("returned g and rhs from vertex data:", dat)
    return dat


def gu_greater_than_rhsu(u):
    g,rhs = get_g_and_rhs(u[0]) 
    if g > rhs:
        return True
    elif g == rhs:
        print("duitai barabar")
    else:
        print("ye kya huwa?")
    return False





def computeshortestpath():
    ut = utopkey() 
    # print("---------------",ut)
    calkey = CalculateKey(all_state_data[14])
    # print("---------------",)
    print("---------------",calkey)
    rhs_s_start = all_state_data[14][1][1]
    g_s_start = all_state_data[14][1][0]  

    if ut == None:
        ut = 0
    print(ut,calkey[0],calkey[1])

    if calkey[0] == np.inf and calkey[1] == np.inf:
        flag = True


    while ( flag or ( rhs_s_start > g_s_start ) ):
        u = utop()
        k_old = utopkey()
        print(k_old)
        k_new = CalculateKey(u)
        if k_old < k_new :
            u_update(u,k_new)

        elif gu_greater_than_rhsu(u):
            x, y = u[0]
            position = y * 5 + x
            g,rhs = all_state_data[position,1]
            all_state_data[position][1][0] = all_state_data[position][1][1]   #g(u) = rhs(u)
            remove_element(u[0])

            results = pred(position)
            for result in results:
                if (result != 0):
                    all_state_data[result][1][1] = min(all_state_data[result][1][1], 1 + all_state_data[position][1][0])
                    updatevertex(result)
        else:
            print("wtf")


computeshortestpath()





def pred(num):
    numbers = []
    if num + 5 <= 20:
        numbers.append(num + 5)
    if num - 5 >= 0:
        numbers.append(num - 5)
    if num - 1 >= 0:
        numbers.append(num - 1)
    if num + 1 <= 20:
        numbers.append(num + 1)
    return numbers



            











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

fig, axs = plt.subplots(nrows=4, ncols=5)

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