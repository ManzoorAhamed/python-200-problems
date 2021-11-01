# Write a Python program to sum all the items in a list
# Example sum_list([1,2,-8])
# Return -5

## Solution

sum_list = [1,2,-8]
item_total = 0
for i in sum_list:
    item_total+=i
print(item_total)

## Solution2 with function
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))