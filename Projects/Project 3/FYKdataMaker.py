#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import random
import math
import bisect
import matplotlib.pyplot as plt


def find_min(numlist):
    #This function finds the minimum of a list of numbers
    #and returns the position of the (first occurrence of the) minimum
    #Input :
    # numlist : list of numbers to sort
    #Output :
    # position : an index for where the minimum is in the list
    #
    
    temp_pos=0
    temp_val=numlist[temp_pos]
#    print(temp_val)
    for i in range(1,len(numlist)):
#        print(i)
        if numlist[i] < temp_val :#check if numlist[i]<temp_val
            temp_pos = i #if so update temp_pos to i
            temp_val=numlist[temp_pos] #update temp_val
        
    return temp_pos

def FYKdata(numlist):
    #This function finds the reverse FYK permutation for a list of numbers
    #FYK stands for Fisher Yates Knuth
    #Input :
    # numlist : list of numbers to sort
    #Output :
    # FYKlist : list of integers giving the FYK data of the permutation to sort it
    #
    
    temp_numlist = numlist #we define a list for use in this definition
    FYKlist = []; #our output data is this, initialized empty
    for i in range(len(numlist)): #we run the find_min n times n=len(numlist)
        temp_pos = find_min(temp_numlist) #we get the position from find_min
        FYKlist.append(temp_pos) #we append that number to our FYK list data
        temp_numlist.pop(temp_pos) #we pop that term in the temp numlist (remove)
    
    return FYKlist

perm_length = 100 #change this to change the length of your original permutation
perm_pi = np.random.permutation(perm_length) 
#use built in random command to make a (uniform) random permutation
perm_pi_list = perm_pi.tolist() #change the array to just a list
print(perm_pi_list) #we print the random list
FYK_pi_data = FYKdata(perm_pi_list) #apply the reverse FYK algorithm to our perm
print(FYK_pi_data) #we print the reverse FYK data

