# Write a Python program to remove the nth index character from a nonempty string

## Solution

def remove_character(string,n):
    first_part = string[:n]
    second_part = string[n+1:]
    print(first_part+second_part)

remove_character("python",0)

## Solution2
def remove_char(str, n):
      first_part = str[:n] 
      last_pasrt = str[n+1:]
      return first_part + last_pasrt
    
print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))