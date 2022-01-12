# Write a Python program to get the file size of a plain file.
# Use test.txt file at same folder

## Solution 1
import os

file_size = os.path.getsize('/home/arhan/VScode/python-200-problems/42-print-file-size/test.txt')
print("File Size is :", file_size, " bytes")