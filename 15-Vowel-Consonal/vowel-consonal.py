# Write a Python program to check whether an alphabet is a vowel or consonant

## Solution
import re
string=input("Enter the string : ")

for i in string:
    if i.isalpha():
     if re.search("[aeiou]",i):
        print("The string %s is Vowel"%i)
     else:
        print("The string %s is Consonal"%i)

