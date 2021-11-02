# Write a Python function to create the HTML string with tags around the word(s).
# Sample function and result : 
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

## Solution
def add_tags(arg1, arg2):
    print('<'+arg1+'>'+arg2+'</'+arg1+'>')

add_tags("i","Python")
add_tags('b', 'Python Tutorial')

## Solution2
def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)
 
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))