set1={1,2,3}

set1.add(100)
print(set1)
set1.remove(1)
print(set1)
# set1.clear()
# print(set1)

set2=set1.copy()
set2.remove(100)
print(set1)
print(set2)