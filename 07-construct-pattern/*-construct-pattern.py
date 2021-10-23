#  Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

## Solution
for i in range(5):
    print(str("* ") * i, sep=' ')
for i in range(5,0,-1):
    print(str("* ") * i)


## Solution 2
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')