# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.


## Solution
from datetime import date               ## datetime module.

today=date.today()                      ## Todays date.
year=int(today.strftime("%Y"))          ## Fetching the year.

name=input("Enter the Name : ")         ## Enter the name.
age=int(input("Enter the Age : "))      ## Enter the age.

year_100 = (100 - age) + year           ## Calculate the year.

print("%s you will become 100 year's old in the year %d"%(name,year_100))   ## Print Statement.