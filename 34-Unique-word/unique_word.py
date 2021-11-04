# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

## Solution
random_words = "red, white, black, red, green, black"
random_words_list = random_words.split(",")
random_words_list.sort()
unique_words = []
for word in random_words_list:
    if word not in unique_words:
        unique_words.append(word)
unique_words_string = " "
for u_word in unique_words:
    unique_words_string += u_word+", "
print(unique_words_string)

## Solution 2
items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")] ## For loop to conver string into the list
#print(words)
print(",".join(sorted(list(set(words)))))   ## Removed the duplicate formed list and sorted then finally joined