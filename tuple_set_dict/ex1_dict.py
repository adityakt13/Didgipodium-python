contacts = {
    'emergency': '112',
    'woman helpline': '1090',
    'home': '7524979322'
}
print(contacts)
while True:
    print("-->call")
    print("-->exit")
    print("--"*12)
    cnt = input("Do you want to call, add or exit:")
    if cnt == 'call':
        name = input("enter contact name: ")
        if name in contacts:
            print(f"calling {name} at {contacts[name]}")
        else:
            print(f"{name} not found")
    elif cnt == 'exit':
        break
    elif cnt == 'add':
        name = input('Enter name of contact:')
        number = input("Enter number of contact:")
        contacts[name] = number
        print(f"{name} added successfully")
    else:
        print('invalid choice')
    print("__"*10)