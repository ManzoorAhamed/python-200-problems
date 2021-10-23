# Count the number of even and odd numbers from a series of numbers
# Input 
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4                                                                                    
# Number of odd numbers : 5 


## Solution

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even=odd=0
for i in numbers:
    if i%2 == 0 :
        even=even+1
    else:
        odd=odd+1

print("Number of even numbers : %d"%even)
print("Number of odd : %d"%odd)