# Write a Python program to check whether a list contains a sublist.
# Input
# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]
# print(is_Sublist(a, b))
# print(is_Sublist(a, c))
# Output

## Solution

def is_Sublist(list1,list2):
    yes=0
    no=0
    for i in list2:
        if i in list1:
            yes+=1
    if yes == len(list2):
        print("Yes, we have sub list")
    else:
        print("No, we dont have sub list")
            

a = [2,4,3,5,7]
b = [4,7]
c = [3,8]
is_Sublist(a,b)
is_Sublist(a,c) 

## Solution 2

def is_Sublist(l, s):
    sub_set = False
    if s == []:
        sub_set = True
    elif s == l:
        sub_set = True
    elif len(s) > len(l):
        sub_set = False
    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i+n] == s[n]):
                    n += 1
                
                if n == len(s):
                    sub_set = True
 
    return sub_set
 
a = [2,4,3,5,7]
b = [4,3]
c = [3,8]
print(is_Sublist(a, b))
print(is_Sublist(a, c))