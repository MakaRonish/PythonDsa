list1 = [1, 2, 3, 4, 9, 6, 7]
n=len(list1)
#by value
for i in list1:
    print(i)
for i in range(0,len(list1)-1):
    print(list1[i])


for i in range(n-1,-1,-1):
    print(list1[i])

for i in range(-n,0,):
    print(list1[i])

