lst=[1,2,3,4,5,6,23,10]
lst[-1]=200#changing value
for i in range(0,len(lst)):
    if lst[i]%2==0:
        lst[i]=lst[i]+5
    else:
        lst[i]=lst[i]-5
print(lst)

