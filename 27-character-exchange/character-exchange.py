# Write a Python program to change a given string to a new string where the first and last chars have been exchanged 

## Solution

string = "manzoor"
string_list = []

for cha in string:  ## Convert string to list
    string_list.append(cha)
string_list[0], string_list[-1] = string_list[-1], string_list[0]

string = ""
for cha in string_list:
    string+=cha
print(string)

## Solution 2
def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
    
print(change_sring('abcd'))
print(change_sring('12345'))