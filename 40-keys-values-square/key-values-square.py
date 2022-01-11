# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.

## Solution

dic1 = {}
value = ""
for i in range(1,16):
    value = int(i*i)
    dic1.update({i: value})

print(dic1)

## Solution 2
d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)