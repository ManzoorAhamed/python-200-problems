# Write a Python program to create a Caesar encryption
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
# The method is named after Julius Caesar, who used it in his private correspondence.
# plaintext:  defend the east wall of the castle
# ciphertext: efgfoe uif fbtu xbmm pg uif dbtumf

## Solution

def caesar_encrypt(realText, step):
    outText = []
    cryptText = []
    
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
    for eachLetter in realText:
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)
            crypting = (index + step) % 26
            print(crypting)
            newLetter = uppercase[crypting]
            outText.append(newLetter)
        elif eachLetter in lowercase:
            index = lowercase.index(eachLetter)
            crypting = (index + step) % 26
            newLetter = lowercase[crypting]
            outText.append(newLetter)
    print(cryptText)
    return outText
 
code = caesar_encrypt('defend the east wall of the castle', 1)
print()
print(code)
print()

## Solution2

def caesar_encrypt1(realText, step):
    outText = []
    cryptText1 = []
    
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
    for eachLetter in realText:
        if eachLetter in uppercase:
            index = (uppercase.index(eachLetter) + step) % 26
            cryptText1.append(uppercase[index])
        elif eachLetter in lowercase:
            index = (lowercase.index(eachLetter) + step) % 26
            cryptText1.append(lowercase[index])
        else:
            cryptText1.append(" ")
    str = " "
    for letter in cryptText1:
        str += letter
    print(str)
code = caesar_encrypt1('defend the east wall of the castlez', 1)