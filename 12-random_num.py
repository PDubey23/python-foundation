''' Python random module generates random numbers in Python.
Supports integers and floating point random generation
reproducable, pseudo random
'''

# Pick a random element from a list, string or tuple

import random
a = [1, 2, 3, 4,5 ,6]
print(random.choice(a))
print()

# a float between 0 and 1

a = random.random()
print(a)
print()

# Generate random integers in a randint and randrange

for i in range(10): 
    r1 = random.randint(1,10)      #Inclusive end
    print(r1)
print()
for i in range(10): 
    r1 = random.randrange(1,10)      #Exclusive end
    print(r1)
print()




# Using seed() for reproducible output

''' these numbers are reproducible,
not recommended to be used for security purposes
'''

random.seed(5)    #initalise the random number generator
print(random.random())
random.seed(5)
print(random.random())
random.seed(5)
print(random.randint(1,10))
random.seed(5)
print(random.randint(1,10))
print()
random.seed(1)
print(random.random())
random.seed(2)
print(random.randrange(1,10))
random.seed(1)
print(random.random())
random.seed(2)
print(random.randrange(1,10))
print()

# Select Multiple Unique Random Items

from random import sample

a = [1,2,3,4,5]
print(sample(a, 3))

b = (94,5,6,7,8)
print(sample(b, 3))

c = "45678"
print(sample(c, 3))

# Shuffle elements in a list

a = [1, 2, 3, 4, 5]
print(f"Before shuffle: {a}")
random.shuffle(a)
print(f"After shuffle: {a}")

'''Some functions in random module'''

state = random.getstate()
print(state)


fruits = ["apple", "banana", "mango"]

print(random.choices(fruits, k=3))
print()

x = random.uniform(1,10)   #floats between two values
print(x)
print()
x = random.gauss(50, 10) #gauss(mean,std)-> normal distribution
print(x)
print()
x = random.normalvariate(50, 10)
print(x)
print()
x = random.getrandbits(8)
print(x)