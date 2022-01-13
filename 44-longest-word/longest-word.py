# Write a python program to find the longest words in a file
# Using test.txt file in same folder

## Solution 1
import os
file_path="/home/arhan/VScode/python-200-problems/44-longest-word/test.txt"
f=open(file_path,"r")
word=int(0)
for f_line in f.readlines():
    for f_word in f_line.split(" "):
        if len(f_word) > word:
            word=len(f_word)
            l_word=f_word
print(l_word)

## Solution2
def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
print(longest_word(file_path))