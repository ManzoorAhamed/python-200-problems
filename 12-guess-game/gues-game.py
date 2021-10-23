# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 

import random
rand=random.randint(1,9)

print(rand)
A="Y"
while A == "Y":
 guess_number=int(input("Enter the number : "))
 if rand == guess_number:
    print("You guessed right")
 elif rand < guess_number:
    print("too high")
 else:
    print("too low")
 A=input("Do you want to continue Y|N : ")

