# storing text data
from ast import Num
from audioop import add
from re import L


text ="ice cream"
print(text)

# accessing individual characters of a string using index
print(text[0]) 
print(text[1])

# strings are immutable
'''
this will give error
text[0] = 'l'
'''
# instead use replace() to make a new string with changes in the original one
message = "hello world"
newMessage = message.replace("world", "universe") 
print(newMessage)

# extracting sub-string in this main string
print(text[0:3])
print(text[4:])
print(text[:3])

# both are the same thing
a = "bob"
a = 'bob'

# count method in strings
print(a.count('b')) # have to give some argument inside count method

# multiple line strings  = use triple-quotes
address = '''282 Littleton Street
            Crestview North Apartments
            West Lafayette'''

print((address))

# how is this multiple line string being stored?
# this is done using \n (to move to the next line)

# concatination of strings
s1 = "hello"
s2 = "world"
print(s1+ " " + s2)

# cannot concatinate string and number
'''this will give error
s = "total states in the USA are"
num = 50
print(s+num)
'''

# string concatination
s = "total states in the USA are "
num = 50
print(s+str(num))

# a better way to do string concatination
'''
if there are large number of strings that we need to join, using a 
+ sign can be difficult to keep track of, so we use formatted strings
'''
answer = '{}{}'.format(s, num)
answer2 = '{}, {}'.format(s, num)
print(answer)
print(answer2)

# f-strings
answer3 = f'{s}, {num}'
print(answer3)
 
print(help(str))