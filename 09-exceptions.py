'''
SyntaxError                     ZeroDivisionError
TypeError                       IOError
ModuleNotFoundError             IndentationError
NameError                       RunTimeError
FileNotFoundError               StackOverflowError
ValueError                      KeywordInterrupt
IndexError
KeyError
'''

# Raising a error

x = 5
if x<0 :
    raise Exception("x should be positive")

# AssertionError
x = -5
assert(x>=0),'x is not postive'  

'''Syntax:

try:
    #Code
except SomeException:
    #Code
else:        Executes only if no exception occur in try
    #Code
finally:    Runs regardless of what happens useful for
    #Code   cleanup tasks like closing files

'''
n = 10
try:
    res = n/0
except ZeroDivisionError as e:
    print(e)


try:
    a= 5/1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("everthing is changaaa")
finally:
    print("cleaning up the mess....")

class ValueTooHighError (Exception):
    pass

def test_val(x):
    if x>100:
        raise ValueTooHighError('Value is too high')

try:
    test_val(1000)
except ValueTooHighError as e:
    print(e)




a = ['10', 'twenty', 30]
try:
    total = int(a[0]) + int(a[1])
except (ValueError, TypeError) as e:
    print("Error", e)
except IndexError as e:
    print(e)
    

