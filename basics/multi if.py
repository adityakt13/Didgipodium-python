x = input ("Enter a number: ")
y = input ("Enter another number: ")

if x.isnumeric():
    x = int(x)
else:
    print("setting value of x to 0")
    x = 0

if y.isnumeric():
    y = int(y)
else:
    print("setting y to 0")
    y = 0

z = x + y
print (f'total is {z}') # We use f and with variable inside curly braces when we want the value of variable to be printed