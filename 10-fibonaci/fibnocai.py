# Write a Python program to get the Fibonacci series between 0 to 50 

## Solution

## a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
a=c=0
print(a)
b=1
print(b)
while c < 50:
   print(c)
   c=a+b
   a=b
   b=c

## Solution2
x,y=0,1
while y<50:
    print(y)
    x,y = y,x+y
