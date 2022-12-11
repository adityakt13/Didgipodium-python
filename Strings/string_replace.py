msg = '''
A mobile phone, cellular phone, cell phone, cellphone, handphone or pocket phone, sometimes shortened to simply mobile, cell, or just phone, is a portable telephone that can make and receive calls over a radio frequency link while the user is moving within a telephone service area. 
'''

msg2 = msg.replace('o', 'u')
print(msg2)

msg3 = msg.replace('phone', 'drone')
print(msg3)

#replacing limited number of times
msg4 = msg.replace('phone', 'drone', 3)
print(msg4)