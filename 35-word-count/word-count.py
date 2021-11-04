# Write a Python program to count the occurrences of each word in a given sentence 

## Solution
items = input("Enter the words : ")
def word_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

items_list = [word for word in items.split(" ")]
print(word_frequency(items_list))

## Solution 2
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print( word_count('the quick brown fox jumps over the lazy dog.'))