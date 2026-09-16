''' Dictionaries store information in key-value pairs.
    Key must be unique and immutable.
    Values can be mutable or immutable 
    Dictionaries are themselves ordered and mutable.
    Before Python 3.7 dictionaries are unordered.'''

#Creating dict

mydict = {"name" : "Pranjal", "age": 19, "city": "NYC"}
dict2= {}
dict3= dict()
dict4= dict(name="Marry", age= 27, city= "Barcelona")
print(dict4)

dict2["name"] = "Sakshi"
print(dict2)
dict2["email"] = "sakshi12@gmail.com"

#Accessing Dictionary Items

d= {"name": "Hidaya", "age": 19}
print(d["name"])
print(d.get("age"))   

'''Accessing a missing key with [ ] raises a KeyError,
 while get() is safer because it returns None
   (or a default value) instead of an error.
'''


del dict3    #deleting entire dictionary
del dict4["name"]  #deleting key-value pair 
print(dict4)

#Removing Dictionaries Items
mydict.pop("city") #delete and return value.
print(mydict)
print(mydict.popitem())
mydict.clear()

#Iterating through a dictionaries

d= {"a": 1, "b" : 2}
for key in d:
    print(key)

for key in d.keys():    #list of keys
    print(key)

for value in d.values():
    print(value)

for item in d.items() :
    print(item)


#Nested-dictionaries

d= {"student": {"name":"Sam", "age":19}
    }

print(d["student"]["name"])

mydict = {"name" : "Pranjal", "age": 19, "city": "NYC"}
mydict_cpy1 = mydict.copy()
mydict_cpy2 = dict(mydict)

mydict3= {"name": "Hidaya", "age": 19, "email": "hidaya@gmail.com"}

mydict3.update(mydict)
print(mydict3)
