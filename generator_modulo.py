#Goal is to find generator of Zn(Integer Modulo). Under addition, it is <1,+>
#This function finds generator of finite Zn under multiplication.
# Before we begin, generator is not necessarily unique.

import math

#Define modulo n
Zn = 8

#temporary store result of generated elements
temp_array=[]

#computation
for generator in range(Zn):
    for i in range(Zn):
        temp_array.append(generator*i % Zn)
        
    #Check if current generator is the generator
    temp_array.sort()

    if(temp_array == [i for i in range(Zn)]):
        print("Answer of generator is ",generator)
        temp_array.clear()
    else:
        temp_array.clear()


#For example, if Zn = 8, generator is 1,3,5,7
# and they are all relatively prime to 8.
