dict1 = {
    'home':'8005865810',
    'personal': '7985607814',
    'emergency': '112'
}
while True:
    print('--'*10)
    print(dict1)
    print('--'*10)
    choice = input('Do you want to call, exit or add? :')
    if choice == 'call':
        contact = input("Enter the contact name: ")
        if contact in dict1:
            print(f'calling {contact} at {dict1[contact]}')
        else:
            inp = input('Contact not found. Do you want to add this number? yes/no: ')
            if inp == 'yes':
                contact = input ('Enter contact name: ')
                number = input ('Enter number of the contact:')
                dict1[contact] = number
                print(f'{contact} with number {number} saved ')
            if inp == 'no':
                break
    elif choice == 'exit':
        break
    elif choice == 'add':
        contact = input("Enter name :")
        number = input("Enter number :")
        dict1[contact] = number
        print(f'{contact} added successfully')
    else:
        print('invalid choice')
    print('--'*10)