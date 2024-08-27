def right(num):
    last=num[-1]
    i=len(num)-1
    while i>=0:
        if i==0:
            num[0]=last
        else:
            num[i]=num[i-1]
        i-=1
    print(num)
def left(num):
    last=num[0]
    i=0
    while i<len(num):
        if i==len(num)-1:
            num[-1]=last
        else:
            num[i]=num[i+1]
        i+=1
    print(num)
left([5,1,2,3,4,])
right([5,1,2,3,4,])


        
