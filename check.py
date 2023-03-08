print('ques1')
string1 = "hello i am using python for coding"
new = string1.split(' ')
for i in new:
    print(len(i))

print('ques2')
tuple1 = ('one','two','three','four','five',6,7,8,9)
tuple1 = list(tuple1)
tuple1[int((len(tuple1)-1)/2)] = 300
print(tuple(tuple1))

print('ques3')
num1 = [1,2,4,6,8,10,12]
sum1 = sum(num1)
mean = sum1/len(num1)
medianind = int(len(num1)/2 )
median = num1[medianind]
print(mean)
print(median)

print('ques4')
list1 = [1,2,3,4,5,1,2,3,4]
set1 = set(list1)
list2 = list(set1)
print(list2)

print('ques5')

string1 = 'Hello I am using python to do whatever I want'
revstring = string1[::-1]
print(revstring)