l=[23,45,65,334,34,45,46,45645]
n=len(l)
total=0
def sum(total)->int:
    # total=0
    for i in range(0,n):
        if l[i]%2==0:
            total+=l[i]
    return total
print(sum(total))
total1=0
def sumindex(total1)->int:
    # total=0
    for i in range(1,n,2): 
        print(i)
        total1+=l[i]
    return total1
print(sumindex(total1))

