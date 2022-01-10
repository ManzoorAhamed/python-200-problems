# Check if a given key already exists in a dictionary
# input
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# is_key_present(5)
# is_key_present(9)
# output
# Key is present in the dictionary                                                                              
# Key is not present in the dictionary

## Solution
def is_key_present(n):
    d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    key = d.keys()
    if n in key:
        print("Key is present in the dictionary")
    else:
        print("Key is not present in the dict")

is_key_present(5)
is_key_present(9)

#### Solution 2
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)