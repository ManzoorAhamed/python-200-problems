# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6 
# Digits 2


## Solution


data=input("Enter the data : ")
alpha=0
num=0
for i in data:
    if i.isalpha():
        alpha=alpha+1
    elif i.isdigit():
        num=num+1

print("Letter : %d"%alpha)
print("Number : %d"%num)

