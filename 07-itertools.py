''' Itertool provide various functions that work on iterators
to produce complex iterators, forms iterator algebra
'''

import operator 
import time

a = list(range(1, 10001))
b = list(range(1, 10001))

num_iterations = 5
mapt = []
loopt = []

#the underscore (_) is a special variable name used to
#indicate that a value is temporary or insignificant
for _ in range(num_iterations):   
    t1 = time.time()
    result = list(map(operator.mul, a,b))
    t2 = time.time()
    mapt.append(t2 - t1)


for _ in range( num_iterations):
    t1 = time.time()
    result = [a[i] * b[i] for i in range(len(a))]
    t2 = time.time()
    loopt.append(t2 - t1)


avg_mpt = sum(mapt) / num_iterations
avg_loopt = sum(loopt) / num_iterations

print(f"Average time of map: {avg_mpt:.6f} seconds")
print(f"Average time of loop: {avg_loopt:.6f} seconds")


''' Infinite iterators -
1. count(start, step)
2. cycle(iterable)
3. repeat(val, num)
'''
# 1. count

from itertools import count

for number in count(start=1, step=2):   #float value can be passed
    if number<10:
        break
    print(number)

counter = count(start=5, step=5)
print(next(counter))
print(next(counter))

for i in count(5, 5):
    if i== 35:
        break
    print(i, end= ' ')
print('\n')



# 2. cycle

from itertools import cycle

count = 0
for i in cycle('ABC'):
    if count== 9:
        break
    else:
        print(i, end= ' ')
        count+=1

counter = cycle('123')
print(next(counter))
print(next(counter))
print(next(counter))

# repeat(val, num)

from itertools import repeat

print(list(repeat(25,6)))

counter = repeat(2)    #stream of constant value
print(next(counter))
print(next(counter))
print(next(counter))



''' Combinatoric iterators-are generators designed to simplify
the creation of mathematical arrangements like permutations,
combinations, and Cartesian products.'''

#1. product()
from itertools import product

a = [1,2]
b = [3,4]
cart_pdt = product(a,b)
print(list(cart_pdt))

print(list(product([1,2], repeat=3)))
print(list(product(['geeks', 'for', 'geeks'], '2')))
print()

print(list(product('AB', [3,4])))


#2. permutations()
from itertools import permutations
a = [0,1,2]
per = permutations(a)
print(list(per))
print()
print(list(permutations([1,'pranjal'], 2)))
print()
print(list(permutations("AB")))
print()
print(list(permutations(range(3), 2)))
print()

#3. Combinations()

from itertools import combinations, combinations_with_replacement 

print(list(combinations(['a', 'b', 'c', 'd'], 2)))
print()
print(list(combinations_with_replacement(['a', 'b', 'c', 'd'], 2)))
print()
print(list(combinations('AB', 2)))
print()
print(list(combinations(range(2),1)))
print()

'''Terminating iterators are used to work on the short input 
sequences and produced the output based on the functionality 
of the method used'''

# 1. accumulate(iter, func)    default func: addition

import operator
from itertools import accumulate

l1 = [1, 3, 6, 9]
print("The sum after each iteration is: ", end= "")
print(list(accumulate(l1)))

print(list(accumulate(l1, lambda x,y: x*y)))
print(list(accumulate(l1, operator.mul)))

# 2. chain(iter1, iter2, ...)

'''If the lists contains millions of values than joining
them through concatenation'''

from itertools import chain
l1 = [1,3,4,5]
l2 = ['A', 'B', 'C']
l3 = [8,10,6]
combined = chain(l1, l2, l3)
print(list(combined))

#3. islice(iterable, start, stop, step)
'''For iterators that are too large to store in memory
in list format, we use islice to get desired slice
 '''
from itertools import islice, count
result = islice(range(10), 5)
print(list(result))
print()
print(list(islice(range(15),1,10,2)))
print()
print(list(islice(count(0,2),24,38)))
print()


with open('test.log', 'w') as f:
    f.write("Log line 1: Initialization\n")
    f.write("Log line 2: Loading resources\n")
    f.write("Log line 3: Processing data\n")
    f.write("Log line 4: This line will be skipped\n")

with open('test.log', 'r') as f:
    header = islice(f, 3)     # a file is itself an iterator

    for line in header:
        print(line)     #first three lines


# 4. compress(iter, selector)
from itertools import compress
letters = ['a', 'b', 'c', 'd']
selectors = [True, True, False, True]

result = compress(letters, selectors)
print(list(result))
print()
print(list(compress('Pranjal Dubey', [1,1,0,0,0,1,1,1,1,1,1,0,0,1])))
print()


# 5. filterfalse(func, seq)

from itertools import filterfalse
def lt_2(n) :
    if n<2:
        return True
    return False

print(list(filter(lt_2,[1,-2,3,-2,2,1,0])))
print()
print(list(filterfalse(lt_2,[1,-2,3,-2,2,1,0])))
print()


# 6. groupby(iterable, key)

from itertools import groupby

a = [1,2,3,4]
result = groupby(a, key= lambda x: x<3)

for key, value in result:
    print(key, list(value))


# 7. map(function, iterable) and starmap(func.,tuple list)

from itertools import starmap, repeat

squares = map(pow, range(10),repeat(2))
print(list(squares))
print()
# numbers = list(map(int, input("Enter numbers: ").split()))



squares = starmap(pow, [(0,2), (1,2), (2,2)])
print(list(squares))

                  


