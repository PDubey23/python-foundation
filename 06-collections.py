'''collections module provides specialized containers-
Counter, OrderedDict, defaultdict, deque, namedtuple

immutable->hashable
hashable -> strings, integers, floats, booleans
and tuples(only contain hashable items)
unhashable -> dictionaries, sets and lists
'''

#Counter is a sub-class of the dictionary.(to count hashable items) 
'''It keep the count of the element in an iterable in 
the form of the unordered dictionary'''

from collections import Counter

#Initialising Counter objects

print(Counter(['B', 'A', 'A', 'C', 'D','D','A','B','D',1,2,2,3,5,1]))
print(Counter({'A':3, 'B':5, 'C':2}))
print(Counter(A=3, B=5, C=2))

my_counter = Counter('aaaaaaabbbbbcccccccccddddd')
print(my_counter)
print(my_counter.most_common(2))
list_count = list(my_counter.elements())
print(list_count)
print(my_counter.total())

my_counter.update('aaaxyz')
print(my_counter)

my_counter.subtract({'a':4,'x':3})
print(my_counter)


#OrderedDict
'''OrderedDict is a dictionary that preserve the order 
in which the keys are inserted
While regular dictionaries do this from Python 3.7+
'''

from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

print(od)

''' 2 OderedDict objects with same items will
return false on equality check'''

print('Before Deleting')
for key, value in od.items(): 
    print(key, value) 
od.pop('a')
od['a'] = 1

print('\nAfter re-inserting')
for key, value in od.items(): 
    print(key, value)


#defaultdict

'''defaultdict is a subclass to dictionary
It provide some default values for the key
that does not exist and never raises a KeyError
'''

from collections import defaultdict

d = defaultdict(int)
L = [1,2,3,2,4,1,2]
for i in L:
    d[i] += 1   # default is 0

print(d)

d2 = defaultdict(list)

for i in range(5) :
    d2[i].append(i)

print(d2)


# namedtuple

''' Instead of using indexes, you can access 
elements by named fields
'''
from collections import namedtuple
# namedtuple(typename, field_names)
#Declaring namedtuple
Student = namedtuple('Student', ['name', 'age', 'DOB'])

S = Student('Nandini', 19, 2541997)
print(S[1])
print(S.name)

Point = namedtuple("Point", 'x, y')   # class Point with fields x and y
pt = Point(-1, 4)
print(pt)


#deque (double-ended queue)

'''time-complexity for append and pop 
list -> O(n)
deque -> O(1)
deque act as FIFO(queue) and LIFO(stack)
'''

'''Declaring deque
deque(list)'''

from collections import deque

queue = deque(['name', 'age', 'DOB'])
print(queue)

de = deque([1, 2, 3])
de.append(4)
print(de)

de.appendleft(6)
print(de)

de.pop()
print(de)

de.popleft()
print(de)








