ques = "What is an Elephant"
oA = "A mammal"
oB = "An insect"
oC = "A bird"
oD = "A reptile"
correct = "A"
print ("Welcome to the quiz")
print (ques)
print('-' *10)
print(f'a) {oA}')
print(f'b) {oB}')
print(f'c) {oC}')
print('d)',oD)

ans = input ("Enter your answer- ")
if ans.upper() == correct:
    print("Correct")
else:
    print ("Wrong")