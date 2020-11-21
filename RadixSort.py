# -*- coding: utf-8 -*-
"""
Radix Sort
Implemented using Count Sort for individual digit sorting 

@author: Denis
"""


#Sorts a given list using Radix Sort
#Uses Count sort for individual digits
def radix_sort(input_list):
    #Works on numbers less then 1M, increase second value to sort larger numbers 
    for index in range(1, 7):
        input_list = count_sort(input_list, index)
        
    return input_list
        
#Returns 1 digit number at (digit/index) of a bigger number -> ex 5478 @ digit 3 = 4
def getDigit(num, digit):
    working = num // (10** (digit-1) );
    return working % 10;

#Returns sorted list -> Stable algorithm
#Sorts based on index of digit param
def count_sort(input_list, index):
    
    original_copy = input_list.copy()
    
    input_list = make_1d(input_list, index)
    occurences = num_occurences(input_list)
    #print(occurences)
    occurences_cummulative = sum_with_previous(occurences)
    #print(occurences_cummulative)
    indexes = shift_right(occurences_cummulative)
    #print(indexes)
    sorted_list = make_final_sorted(indexes, original_copy, index)
    #print(sorted_list)
    
    return sorted_list
    
#Makes an array with only values at proper index of original array
def make_1d(input_list, index):
    out = []
    for i in input_list:
        out = out + [getDigit(i, index)]
    return out

    
#Function that returns number of occurences of each num in array
def num_occurences(input_list):
    
    occurences = [0] * 10 
    
    for i in input_list:
        occurences[i] = occurences[i] + 1
        
    return occurences

#Array with value of current index plus sum of all previous indexes
def sum_with_previous(input_list):
    total = 0
    
    for i in range(10):
        input_list[i] = input_list[i] + total
        total = input_list[i]
        
    return input_list

#Shifts array one to the right
def shift_right(input_array):
    
    for i in range(9, 0, -1):
        input_array[i] = input_array[i-1]
        
    input_array[0] = 0
    
    return input_array
        
#Uses input list, which gives start index of each number, to sort the orginal list based on given index
def make_final_sorted(input_list, original, index):
    out = [0] * len(original)
    
    for i in original:
        adjusted = getDigit(i, index)
        #prob is because you have to do original @ one index
        out[input_list[adjusted]] = i
        input_list[adjusted] = input_list[adjusted] + 1
        
    return out
        

test_list = [104546, 241693, 14564, 102, 458792, 546, 0, 999999]
sorted = radix_sort(test_list)
print(sorted)




