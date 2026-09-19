'''Lambda functions are small anonymous(inline) functions
Used to pass simple logic to another fucntions
USed as an argument for higher order functions
'''
# lambda arguments: expression
'''Contain only one expression
Result of that expression is return automatically
'''

add10 = lambda x: x+10
print(add10(10))
mult = lambda x,y: x*y
print(mult(4,3))

str = 'AmoreFati'
upper = lambda x: x.upper()
print(upper(str))

#Condition checking

check = lambda x: "Positive" if x>0 else "Negative" if x<0 else "Zero"
print(check(5))
print(check(0))
print(check(-5))

#List Comprehension

func = [lambda arg=x: arg*10 for x in range(1,6)]
for i in func:
    print(i())

# Returning multiple results

calc = lambda x,y: (x+y, x*y)
res  = calc(3, 4)
print(res)

#filter(function, iterable)

c = [1,2,3,4,5,6]
even = filter(lambda x: x%2==0, c)
print(list(even))

#map(function, iterable)

def double(val :int) :
    return val*2

a = [1, 2, 3, 4]
res = list(map(double, a))
print(res)

res = list(map(lambda x: x*2, a))
print(res)

a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x,y: x+y, a, b)
print(list(res))

# reduce()

from functools import reduce

a = [2, 4, 6, 8]
r = reduce(lambda x, y: x+y, a)   #((2+4)+6)+8
print(r)


point2d = [(1,2), (15,1), (5,-1), (10,4)]
point2d_sorted = sorted(point2d)
print(point2d_sorted)

point2d_sorted = sorted(point2d, key= lambda x: x[1])
print(point2d_sorted)

