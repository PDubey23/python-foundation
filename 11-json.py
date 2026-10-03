'''JavaScript Object Notation(JSON) is a lightweight format to represent 
structured data
In python, JSON data is usually represented as a string
'''

#Encoding or Serialization
#Python objects -> JSON strings
import json

person = {
    'name': 'Pranjal',
    'age': 20,
    'city': 'NewYork',
    'hasChildren': False,
    'titles': ['AI Manager', 'Python Developer']
}

personJSON: json = json.dumps(person, indent = 4,sort_keys = True)
print(personJSON)
print(type(personJSON))

#json.dump(dict, file_pointer)

with open("person.json", 'w') as file:
    json.dump(person, file, indent= 4)

# Decoding or Deserialization

#json.loads(json_string)

employee = '''{
"name": "Meet",
"department":"AIML",
"company":"Nvidia"
}'''

emp_dict = json.loads(employee)
print(emp_dict)
print(type(emp_dict))


#json.load(file_object)

with open('person.json') as json_obj:
    person = json.load(json_obj)
print(person)


class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

user1 = User('Sakshi',20)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}

    else:
        raise TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(user1, default = encode_user)




from urllib.request import urlopen, Request

url = "https://jsonplaceholder.typicode.com/users"

request = Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

with urlopen(request) as response:
    source = response.read()

data = json.loads(source)

print(data)

print(data[0]['id'])

item = data[3]

street = item["address"]["street"]
suite = item["address"]["suite"]
city = item["address"]["city"]
website = item["website"]
lat = item["address"]["geo"]["lat"]

print(f"{street} {suite} {city} {website} {lat}")





