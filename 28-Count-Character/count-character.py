# Write a Python program to count the number of characters (character frequency) in a string.
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

## Solution 
text = "google"
character_list = set(text)
final_result = {}

for item1 in character_list :
    count = 0
    for item2 in text:
        if item1 == item2 :
            count+=1
    final_result[item1] = count
print(final_result)

## Solution 2
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google'))