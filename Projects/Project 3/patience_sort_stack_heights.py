

import numpy as np
import random
import math
import bisect
import matplotlib.pyplot as plt


def patience_sort(permlist):
    #This function creates a multi-dimensional array
    #containing all of the stacks
    #of the patience sorting algorithm
    #Input :
    # permlist : list of numbers to sort
    #Output :
    # stacks : a list of lists of integers
    #
    # Each entry in stacks is a list of integers, 
    #which are the card values in that stack 
    
    stacks = []
    for x in permlist : #iterate through list of numbers
        temp_stack = [x]
        i = bisect.bisect_left(stacks, temp_stack)
        #determines where number should be inserted if
        # it was to be inserted in order
        if i != len(stacks) :
            # if number is not larger than all numbers on top

            #of stacks
            stacks[i].insert(0,x) #put number on appropriate stack
        else :
            stacks.append(temp_stack) #create new stack
        
    return stacks

perm_length=100 #change this to change the length of permutation
perm_pi = np.random.permutation(perm_length) 
#use built in random command to make a (uniform) random permutation
perm_pi_list = perm_pi.tolist() #change the array to just a list
card_stacks = patience_sort(perm_pi_list) #performs patience sorting on perm_pi_list

#print(card_stacks) #show what the actual card stacks are
#un-comment the line above if you want the program to print out the actual stacks

# Now we will run a short set of commands to 
#get the lengths of each stack instead
stack_heights=[] #initialize it with empty list
for i in range(len(card_stacks)):
    stack_heights.append(len(card_stacks[i]))
    
print(stack_heights)
