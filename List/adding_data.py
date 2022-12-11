x =[] #empty list

x.append(2)
x.append(5)
print(x)
x.append(10)
print(x)

for i in range (11,16):
    x.append(i)
print(x)

y = [23,45,67,52,85]
x.append(y) # it will create  another list inside existing list
print(x)

x.extend(y) # it will add the data in last
print(x)

x.insert (0,'Hello') # will insert 'hello' at index 0
x.insert (27,'Aditya') # if index is out of range then it will add element in the last
print(x)