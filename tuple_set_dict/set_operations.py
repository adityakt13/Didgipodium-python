x = {1,2,3,4}
y = {3,4,2,5,1,5,2,8,6}
ans = x.union(y)
print(ans)

ans1 = x.intersection(y)
print(ans1)

ans2 = x.difference(y)
print(ans2)

ans3 = y.symmetric_difference(x)
print(ans3)

ans4 = x | y # same as union
print(ans4) 

ans5 = x & y # same as intersecion
print(ans5)

ans6 = y - x # same as difference y.difference(x)
print(ans6)

ans7 = y ^ x # same as y.symmetric_diffrence(x)

z ={10,11,12,13}
print('disjoint sets')
print("Do x and y don't have something in common",x.isdisjoint(y))
print("Do x and z don't have something in common",x.isdisjoint(z))
print("Do z and y don't have something in common",z.isdisjoint(y))

items = {'apple', 'orange', 'banana', 'potato', 'tomato', 'brinjal'}
fruits = {'apple', 'orange', 'banana'}
vegetables = {'potato', 'tomato', 'brinjal', 'cucumber'}

print('subset')
print('fruits belong to item', fruits.issubset(items))
print('vegetable belong to item', vegetables.issubset(items))

print('_____'*8)
print('superset')
print('vegetable belong to item', items.issuperset(vegetables))