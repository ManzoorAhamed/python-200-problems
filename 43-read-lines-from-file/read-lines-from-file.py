# Write a Python program to read first n lines of a file.
# Use test.txt file

## Solution 1
import os
f = open("/home/arhan/VScode/python-200-problems/43-read-lines-from-file/test.txt")
lines = 5  ## File name and the lines can be user input
for x in f:
    if lines > 0:
        lines -= 1
        print(x)

## Solution 2
def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
                        
file_read_from_head('/home/arhan/VScode/python-200-problems/43-read-lines-from-file/test.txt',2)