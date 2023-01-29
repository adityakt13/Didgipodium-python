def contp ():
    contact = input("Enter contact's name: ")
    number = input("Enter contact's number: ")
    dict1[contact] = number
    print(f"{contact} with number {number} added successfully.")
    
dict1 = {"home":"8004995810",
        "personal":"7905602714",
        "bhaiya":"9889144254",
        "papa":"9956412701"}
while True:
    print("---"*20)
    print(dict1)
    print("---"*20)
    choice = input("Do you want to call, add or exit: ")
    if choice == "call":
        contact =input("Enter contact name: ")
        if contact in dict1:
            print (f"calling {contact} on {dict1[contact]}")
        if contact not in dict1:
            contnot = input(f"No contact found named {contact}, do you want to add {contact} in your contact's list? (yes/no): ")
            if contnot == 'yes':
                contp()
            if contnot == 'no':
                print("Programme exited successfully.")
                break
    elif choice == "add":
        contp()
    else:
        if choice == "exit":
            print("Programme exited successfully.")
            break
        # this programme was in tuple_set_dict and ask sir how to make this programme short