l1=[1,2,3,4,5]
l2=[-5,2,3,-0,9]
def adding(l,l2):
    result=[]
    n=len(l1)
    for i in range(n):
        result.append(l1[i]+l2[i])
    print(result)

adding(l1,l2)
