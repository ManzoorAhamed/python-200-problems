# Write a Python program to iterate over dictionaries using for loops.

## Solution
d = {'x': 10, 'y': 20, 'z': 30} 

for key in d:
    print(key, 'corresponds to', d[key])

## Solution 2
for dict_key, dict_value in d.items():
    print(dict_key,'->',dict_value)