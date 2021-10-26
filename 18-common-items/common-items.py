# Write a Python program to find common items from two lists.
# input
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# output
# {'Green', 'White'}

## Solution  # Not the expected result.

color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
color3=[]

for item in color1:
    for item2 in color2:
        if item == item2:
            color3.append(item)
print(color3)

## Solution 2

color1 = "Red", "Green", "Orange", "White"      ## what is set in python?
color2 = "Black", "Green", "White", "Pink"
print(set(color1) & set(color2))                ## A set is a collection which is unordered, unchangeable, and unindexed. Sets are written with curly brackets.