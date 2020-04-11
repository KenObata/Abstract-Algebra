#Abstract Algebra:
# This program finds generator of cross product group.


#initialize
Z2=[0,1] #Z1={ [0], [1]}
Z3=[0,1,2] #Z1={[0],[1],[2]}

#all combination Z2 x Z3
Z2_x_Z3=[]
for i in Z2:
    for j in Z3:
        Z2_x_Z3.append([i,j])

print("Group is:",Z2_x_Z3)

#guess and check
temp_list=[]
for generator in Z2_x_Z3:
    print("current generator is:",generator)
    for i in range(len(Z2)):
        for j in range(len(Z3)):
            x=generator[0]*i % len(Z2)
            y=generator[1]*j % len(Z3)
            temp_list.append([x,y])
    print(temp_list)
    if(temp_list == Z2_x_Z3):
        print("Answer of generator is",generator)
        temp_list.clear()
    else:
        temp_list.clear()


