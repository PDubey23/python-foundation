'''Strings are ordered, immutable sequence of characters
  (Tuples, Lists and Strings are Python Sequences.)
  
  '''
a = 'Amor Fati'
b = "Vae Victus"
c = 'I\'m a python programmer.'
print(a, b ,c, sep= '\n')

#Multi-line string 
sentence = """" I am learning    
Python Strings"""     #Newlines are preserved.

#Accessing characters in string

mystring = "Hello World!"

char = mystring[0]
substr = mystring[2:11:2]   #Index out of range -> IndexError
print(char, substr, sep = '\t')

# mystring[0] = 't'   TypeError

greeting = "Hello"
name = "Tom"
sentence = greeting + ' ' + name   #String Concatenation
print(greeting*3)   #String Repetition
for char in sentence:
    print(char, end= ' ')
print('\n')

# String Immutability 
s = "aBCDEF"
print(id(s))
s = "A" + s[1:]
print(s) 
print(id(s))    
'''Any modification to a string creates a new 
string instead of altering the original string
'''

#Deleting a string
s = "ABCDE"
del s
#print(s)     NameError


#String Membership Testing
s = "I\'m a Python Developer"
print('Python' in s)
print('a  ' in s)

# Methods in String

mystring = "    I'm a Python Developer.    "
stripped = mystring.strip()   #Remove leading and trailing whitespaces
print(stripped)

mystring = "eeeeeeI'm a Python Developer.    "
stripped = mystring.strip('e')
print(stripped)
mystring = stripped

upper = mystring.upper()
lower = mystring.lower()
title = mystring.title()
print(upper, lower, title, sep= '\n')


print(repr(mystring))    #Print raw version of string repr()
mystring = mystring.strip()
print(repr(mystring))
print(mystring.startswith('I'))
print(mystring.endswith('Developer.'))
print(mystring.find('o'))
print(mystring.find('eve'))
print(mystring.count('e'))

s= "Python is fun"
print(s.replace("fun", "awesome"))  #No error if old substring is not in the string
print(s)

sentence = "how are you doing?"
mylist = sentence.split() #default_arg = ' '
print(mylist)

sentence = "how,are,you,doing?"
mylist = sentence.split(',')
print(mylist)

for word in sentence.split(','):
    for letter in word:
        print(letter)

newstr = ''.join(mylist)
print(newstr)
print(' '.join(mylist))


#string concatenation vs using join()
from timeit import default_timer as timer
mylist = ['a']*6000
start = timer()
mystr = str()
for char in mylist:
    mystr += char
stop = timer()

print(stop-start)

start = timer()
mystr = ''.join(mylist)
stop = timer()

print(stop-start)

print("Michael Jackson \\M.J.\n")
print(r"Michael Jackson \M.J.\n")   # r means rawstring

#Formatting Strings

# %, format(), f-strings

# % formatting
var1 = "Tom"
mystring = "the variable is %s"%var1
print(mystring)

var2 = 3
var3 = 2.4
mystring = "the variables are %d and %f"%(var2, var3)
print(mystring)

# .format()

mystring = "the variables are {}, {} and {:.2f}".format(var1,var2,var3)
print(mystring)

# f-string formatting

mystring = f"the variables are {var1}, {var2} and {var3}"
print(mystring)

#Output: 
print(mystring)
'''the variables are 3 and 2.400000
the variables are Tom, 3 and 2.40
the variables are Tom, 3 and 2.4'''

