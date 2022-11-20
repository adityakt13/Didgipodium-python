username = input("enter your username: ")
email =input("enter your email: ")
pwd = input("enter password: ")
cpwd = input("confirm password: ")

if len(username)> 0 and username.isalnum():
    if len(email)> 0 and '@' in email:
        if len(pwd)>=4:
            if pwd == cpwd:
                print('Registration successful')
            else:
                print ('Passwords do not match')
        else:
            print('Password must be atleast of 4 characters') 
    else:
        print('Invalid email')
else:
    print("username is invalid.")