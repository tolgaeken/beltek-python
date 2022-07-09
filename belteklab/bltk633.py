list1=[1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,4,4,5,5,6,7,8]
set1 = set(list1)
print(list1)
print(set1)
set1.add(1)
print(set1)
# set1.clear()
# print(set1)
set2 = set([5,6,7,8,9,10])

list3 = [11,12,13,14,15]
set4 = set(list3)

# set3 = set1.copy
# print(set3)

print(set1-set2)

print(set1.difference(set2))
print(set1.intersection(set2))
print(set1.union(set2))