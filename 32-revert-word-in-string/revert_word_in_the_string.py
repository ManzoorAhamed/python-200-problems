# Revert the sentence.
# input : "The quick brown fox jumps over the lazy dog."
# output : "dog. lazy the over jumps fox brown quick The "

## Solution
def revert_sentence(arg1):
    arg1.reverse()
    return arg1

sentence = "The quick brown fox jumps over the lazy dog."
print(revert_sentence(sentence.split(" ")))

## Solution2
def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
    
print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words("Python Exercises."))