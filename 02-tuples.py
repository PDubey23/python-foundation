''' Tuples are ordered but immutable.
    Allows duplicate elements.
    Heterogenous '''

#Creating a Tuple

mytuple=("Max",28,"Boston")
tup2= tuple("Meet")
tup3=tuple()
tup4=(3,)
tup5= "Hidaya",20,"Casablanca"       #Parenthesis are optional.

print(type(tup5))

print(tup5[0])
#tup5[0]= "X"     TypeError: 'tuple' object does not support item assignment

for i in tup5 :
    print(i, end='      ')

tup= tuple("Hidaya")
print(tup[0])
print(tup[1:4])
print(tup[ :3])

#Tuple Unpacking

name, age, hometown = tup5
print(name,age,hometown)

#Concatenation of tuples

tup1=(0,2,4,6,8,10)
tup2= ("Dead", "Poets", "Honour")
print(tup1 + tup2)

#Deleting a tuple
tup= (1,2,3,4,5,6)
del tup
#print(tup)   NameError

#Tuple Unpacking with Asterisk(*)

tup= (1,2,3,4,5)
a, *b, c = tup     #Grabbing multiple items in a list.
print(a, b, c)

# Creating NamedTuple

from collections import namedtuple
Point= namedtuple("Point", ["x", "y"])   #Type: namedtuple and fields x and y
p= Point(x=1, y=2)
print(p.x, p.y)

import sys
mylist = [0, 1, 2, "Hello", True ]
mytuple = (0, 1, 2, "Hello", True)

print(sys.getsizeof(mylist),"bytes")     # 104 bytes
print(sys.getsizeof(mytuple),"bytes")    # 88 bytes


import timeit
print(timeit.timeit(stmt = "[1,2,3,4,5]", number = 1000000))
print(timeit.timeit(stmt = "(1,2,3,4,5)", number = 1000000))

'''Working with Tuples can be more efficient than working with Lists'''




