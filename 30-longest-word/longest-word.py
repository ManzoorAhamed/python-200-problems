# Write a Python function that takes a list of words and returns the length of the longest one 

## Solution
def find_longest_word(arg1):
    a=0
    word=""
    for arg in arg1:
        if len(arg) > a :
            a = len(arg)
            word = arg
    print(word)

list_arg = ["PHP", "Exercises", "Backend"]
find_longest_word(list_arg)

## Solution2
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]
print(find_longest_word(["PHP", "Exercises", "Backend"]))