# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615


## Solution

number=input("Enter the integer number : ")

expected_result=int(number)+int(number*2)+int(number*3)

print(expected_result)