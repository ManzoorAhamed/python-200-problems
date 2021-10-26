# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

## Solution
a=input("Enter the side1 : ")
b=input("Enter the side2 : ")
c=input("Enter the side3 : ")

if a == b and b == c:
    print("Its an equilateral triangle")
elif a != b and b != c and c != a:
    print("It's a scalene triangle")
elif a == b or a == c:
    print("Isosceles triangle")
else:
    pass