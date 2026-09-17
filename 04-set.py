'''Set is a collection of unique items/elements
Unordered, mutable, heterogenous
support fast search, insertion and deletion operations using hashing internally
'''

# Creating set

set1 = {1,2,3,4,3,5}
set2 = set("ABCDE")    #type casting
set3 = set([1,2,3])
set4 = {}     # < class 'dict' >
set5 = set()   # empty set
set6 = {True, 20, 53.7, "Pranjal"}
print(set1, set2, set3)

# Check unique and immutable

s = {20,10,20,10}
print(s)

#s[1] = 2
#print(s)      TypeError: 'set' does not support item assignment

# Frozen Sets
'''Immutable version of sets
Methods such as add() and remove() cannot be used.'''

s = set(["a", "b", "c"])
print("Normal Set: ",s)

fs= frozenset(["e", "f", "g"])
print("Frozen set: ", fs)

# Methods for Sets

s = {"a", "b", "c", "f", "g"}
s.add("d")
print(s)
s.remove("b")  #If not present, KeyError
print(s)
s.discard("e")   #Delete if present


odds = {1,3,5,7,9}
evens = {2,4,6,8,10}
primes = {2,3,5,7,11,13}

u = odds.union(evens)  
print(u)
print(odds|evens)  # '|' for union

i = odds.intersection(evens)
print(i)
print(odds & evens)  # '&' for intersection 

set1 = {1,2,3,4,5,6,7,8,9,12,14,15,16}
set2 = {3,12,5,17,19,1,20}

diff = set1.difference(set2)
print(diff)
print(set1 - set2)  # '-' for difference

sym_diff = set2.symmetric_difference(set1)
print(sym_diff)

set1.update(set2)
print(set1)

set1.intersection_update(set2)
print(set1)

setA = {1,2,3,4,5,6}
setB = {1,2,3}

setA.issubset(setB)
setB.issubset(setA)
setB.issuperset(setA)
setA.superset(setB)
setA.disjoint(setB)





