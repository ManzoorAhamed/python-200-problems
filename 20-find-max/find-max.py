# Write a Python program to get the smallest number from a list.
# max_num_in_list([1, 2, -8, 0])
# return 2

## Solution
max_num_in_list=[1, 2, -8, 0, 5]

def max_num_from_list(max):
    a=0
    for item in max:
        if item > a:
            a = item
    print(a)
max_num_from_list(max_num_in_list)

## Solution 2 
print(max(max_num_in_list))