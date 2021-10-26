# Convert a list of characters into a string
# Input ['a', 'b', 'c', 'd']
# Output abcd

## Solution

list_var = ['a', 'b', 'c', 'd']
str_var = ""

for item in list_var:
    str_var=str_var+item
print(str_var)

## Solution2

s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)   #.join is function which converts list into string
print(str1)