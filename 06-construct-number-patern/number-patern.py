# Write a Python program to construct the following pattern, using a nested loop number.
# 1                                                                                                             
# 22                                                                                                            
# 333                                                                                                           
# 4444                                                                                                          
# 55555                                                                                                         
# 666666                                                                                                        
# 7777777                                                                                                       
# 88888888                                                                                                      
# 999999999  

## Solution

for i in range(1,9):
    print("\n")
    for j in range(i):
        print(i,end="")

## Solution2    Better Solution
for i in range(10):
    print(str(i) * i)