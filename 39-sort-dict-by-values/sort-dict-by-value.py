# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary :  {0: 0, 1: 2, 2: 1, 3: 4, 4: 3}                                                         
# Dictionary in ascending order by value :  [(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)]                            
# Dictionary in descending order by value :  [(4, 3), (3, 4), (2, 1), (1, 2), (0, 0)]

## Solution 1

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

l = list(d.items())
l.sort()
print("Dictionary in ascending order by value : ",l)

l = list(d.items())
l.sort(reverse=True)
print("Dictionary in descending order by value :", l)

## Solution 2
import operator

print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value : ',sorted_d)
