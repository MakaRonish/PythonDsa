l=[10,20,33,47,23,89,90]

def add(lst:list)->int:
    n=len(lst)
    sum=0
    for index in range(1,n-1):
        sum+=lst[index]
    return sum

total=add(l)
print(total)
