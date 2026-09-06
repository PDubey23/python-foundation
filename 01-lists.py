'''Lists are ordered and mutable,
allow duplicate elements,
forward as well as backward indexing'''

#Declaration and Initialization at the same time (in Python)
mylist=[5,True,"apple","apple"]
mylist2=list()

#Indexing
item=mylist[3]
#item=mylist[4]  #IndexError
print(item)

for item in mylist:
    print(item)
    if "apple"== item:
        print("Yes")
    else:
        print("NO")

#Python list stores references to objects.
print(len(mylist))
mylist.append("Lemon")

#Adding elements.
a=[1,2]
a.append(3)
print('\n')
print(a)

a=[1,3]
a.insert(1,5)
mylist.insert(3,"Banana")
print(mylist)
print('\n')
print(a)

a=[1,2]
a.extend({34,5})
print('\n')
print(a)

#Update Elements
a=[22,44,66,90,0,-5]
a[1]=33
print('\n')
print(a)

#Removing elements.
a=[1,2,3,4,1]
a.remove(1)
#a.remove(0)   ValueError
print(a)

a=[2,4,6,8,10]
a.pop()
print(a)
a.pop(3)
print('\n')
print(a)

a=[20,40,60]
a.clear()
print(a)

a=[1,2,3,4,5]
del a[1]
print(a)

a=[20,30,40,None,"Banana"]
a.reverse()
print(a)

'''list.sort() method sorts in-place
sorted() function return a new list
'''

a=[20,30,40,None,"Banana"]
#a.sort()  TypeError
a=[20,25,10,0,-1]
a.sort()
print(a)
a.sort(reverse=False)

mylist=['Apple', 'Banana', 'Watermelon', 'Kiwi']
mylist.sort(key=len)
print(mylist)
mylist.sort(key=len,reverse=1)
print(mylist)

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

users.sort(key=lambda x: x["age"])
print(users)

sorted_users=sorted(users, key=lambda x: x["age"], reverse=True)
print(sorted_users)

#Lists operations

mylist= [0]*5
print(mylist)

list1=[20,21,10,'A','B']
list2=['C','D',11,31,30]
print(list1 + list2)

list1=[20,21,10,]
list2=[11,31,30]
#print(list1 * list2)    TypeError

#Slicing     start:stop:step

mylist=[1,2,3,4,5,6,7,8,9,10]
print(mylist[2:5])
print(mylist[:5])
print(mylist[:])
print(mylist[5:])
print(mylist[:5])
print(mylist[::2])
print(mylist[: :-2])
print(mylist[-1: ])
print(mylist[: :-1])

list_orig=["banana", "cherry", "apple"]
list_copy=list_orig.copy()
print(id(list_orig))  
print(id(list_copy))        #different id

list_cpy=list_orig
print(id(list_orig))  
print(id(list_cpy))         #same id


#List Comprehension

a=[1,2,3,4,5,6]
b=[i*i for i in a]
print(b)









