lst=[5,10,15,22,70,23]

def div(l:list):
    n=len(l)
    for i in range(n-1,-1,-1):
        if l[i]%5==0:
            print(l[i])

div(lst)


