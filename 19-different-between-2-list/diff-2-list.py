# Write a Python program to get the difference between the two lists
# Input 
# list1 = [1, 2, 3, 4]
# list2 = [1, 2]
# Output
# [3,4]

## Solution
list1 = [1, 2, 3, 4]
list2 = [1, 2]
diff=[]
for item in list1:
    if item not in list2:
        diff.append(item)
print(diff)

## Solution2   # its a set not list
print(set(list1) - set(list2))