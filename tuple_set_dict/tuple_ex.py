x = (1,2,3) # tuple
y = 2 ,5, 2, 1 #tuple packing
print(x)
print(y)
print(type(x))
print(type(y))
print(x[0]) # index 0
print(x[1]) # index 1
print(x[-1]) # index -1
z = (1,2,3,4,5,6,7,8,9,10)
print(z[:5]) # slicing

# tuple methods - count , index

a = ('apple', 'apple', 'apple', 'banana', 'pine apple', 'custard apple')
print(f'len of a is{len(a)}')
print(f'Apple occurs {a.count("apple")} times')
print(f'Pine Apple occurs {a.count("pine apple")} times')
print(f'Banana is at index {a.index("banana")} ')

# tuple to list
zl = list(z)
print(type(z), type(zl))
print(z, zl)

#list to tuple
zt = tuple(zl)
print(type(zl), type(zt))
print(zt, zl)

# single item tuple
s = (1,) # comma is important
s2 = 2, # is also tuple
print(type(s))