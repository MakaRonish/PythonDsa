l=[5,-8,10,-15,2,-4,95,-34,25,100]

def max(l:list):
    maxnum=l[0]
    for index in range(1,len(l)):
        if l[index]>maxnum:
            maxnum=l[index]
    return maxnum
def min(l:list):
    minnum=l[0]
    for index in range(1,len(l)):
        if l[index]<minnum:
            minnum=l[index]
    return minnum

highest_num=max(l)
lowest_num=min(l)
print("max=",highest_num)
print("min=",lowest_num)

