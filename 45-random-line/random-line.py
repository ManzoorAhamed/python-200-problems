# Write a Python program to read a random line from a file.
# Using test.txt

## Solution 1
import random

def random_line(afile):
    f = open(afile).read().splitlines()
    return random.choice(f)
print(random_line("/home/arhan/VScode/python-200-problems/44-longest-word/test.txt"))

## Reference : https://www.w3resource.com/python-exercises/file/python-io-exercise-15.php
## Replace the path according to your systemPath