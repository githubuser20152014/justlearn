# Thursday, December 8, 2021

# Take two lists, say for example these two:

# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension.

import random

len_list1 = int(input('how long is list 1: '))
len_list2 = int(input('how long is list 2: '))

list1 = random.sample(range(100), len_list1)
list2 = random.sample(range(200), len_list2)
 
common_list = [i for i in list1 for j in list2 if i == j]

print('List 1 is: ', list1)
print('List 2 is: ', list2)

print('The common elements are: ', common_list)
