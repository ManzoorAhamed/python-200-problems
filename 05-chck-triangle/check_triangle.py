# Write a Python program to check a triangle is valid or not 

## Solution 
# Sum of two sides should be greater than third side.

def triangle_check(s1,s2,s3):
    if (s1 + s2 < s3) or (s1 + s3 < s2) or (s3 + s2 < s1):
        print('No, the lengths wont form a triangle')
    elif (s1 == s2+s3) or (s2 == s1+s3) or (s3 == s1+s2):
        print('Form a degenerated triangle') 
    else:
        print("valid triangle")


## Enter three sides

side1 = input("Enter the side1 :")
side2 = input("Enter the side2 :")
side3 = input("Enter the side3 :")
triangle_check(side2,side2,side3)
