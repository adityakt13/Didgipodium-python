msg = "Journey Before Destination"

msg_upr = msg.upper()
msg_lwr = msg.lower()
msg_cap = msg.capitalize() # capitalizes the first alphabet of string
msg_title = msg.title() # capitalizes each first alphabet of each word 
msg_swapcase = msg.swapcase() # converts uppercase to lowercase and vice versa
msg_casefold = msg.casefold() #same function .lower()

print(msg)
print(msg_upr)
print(msg_lwr)
print(msg_cap)
print(msg_title)
print(msg_swapcase)
print(msg_casefold)

# alignment
print(msg.ljust(50, '|'))
print(msg.rjust(50))
print(msg.center(50))

#alignment with f strings on padding
print(f'{msg:>50}') # same as rjust
print(f'{msg:<50}') # same as ljust
print(f'{msg:^50}') # same as rjust