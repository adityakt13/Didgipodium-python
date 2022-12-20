# creating a dictionary

dict1 = {'Name':'Aditya','Age':20,'Height':178}
print(dict1)

# getting all keys from dictionary
print(dict1.keys())

# getting all values from dictionary
print(dict1.values())

# getting all the items from dictionary as a list of tuples
print(dict1.items())

# nested dict
b = {
    'fruits':{'apple': '5kg', 'custard apple':'3kg'},
    'vegetables':{'cabbage':'2 pieces','tomato':'3kg'},
    'cereals': {'rice': '4kg', 'wheat': '2kg'}
    }
print('------'*10)

from pprint import pp
pp(b)
print(b)
print('keys of b==>', b.keys())
print('values of b==>', b.values())

print('------'*10)

# accessing a value from a dict
print(dict1['Name'])
print(dict1['Height'])
#print(dict1['Weight'])  will give : KeyError: 'Weight'

print('------'*10)

# accessing a value using()
print(dict1.get('Name'))
print(dict1.get('Age'))
print(dict1.get('City','Not found'))
print(dict1.get('Name','Not found'))

print('------'*10)

# traversing a dict
# style 1
for key in dict1 :
    print(key,":", dict1[key])

# style 2
for key, value in dict1.items():
    print(key,value)

# only values
for value in dict1.values():
    print(value)

# only keys
for key in dict1.keys():
    print(key)