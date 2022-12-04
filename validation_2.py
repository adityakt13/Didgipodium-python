a = input("Enter a number: ")
b = input("Enter another number: ")

if a.isnumeric() and b.isnumeric() :
    a,b = int(a),int(b)
    c = a +b
    print(f"The sum is {c}")
else:
    print("Enter numbers only")