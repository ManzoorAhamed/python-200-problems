# Write a Python program to get the frequency of the elements in a list.
# input
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# outout
# {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

## Solution

my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
my_list1 = set(my_list)

final_list = {}

for item in my_list1:
    count = 0
    for item1 in my_list:
        if item == item1:
            count+=1
    final_list[item] = count

print(final_list)

import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)