x = [2,5,1,6,3,6,2,'Hi',"Hello",[1,2,3],5,6,7,9,10]
# remove, pop, clear methods
x.remove(6) # removes the first occurence of 6
print(x)
x.remove(2)
print(x)
if 'hello' in x:
    x.remove('hello')
print(x)
x.remove([1,2,3])
print(x)

x.pop() # removes the last element
print(x)
x.pop(3) # removes the element at index 3
print(x)

x.clear() # empties the list
print(x)