a=[]
def fac(num:int):
    if num==1 or num==0:
        a.append(1)
        return 1
    fa= num * fac(num-1)
    a.append(fa)
    return fa


def less(num):
    fac(num)
    for i in a:
        if i<num:
            print(i)
less(3)

def ja(a=[1,2,3],j=10):
    return a,j

e=ja()
print(e)

print(5//2)
s="asdfghj12345,asdfgh"
l=[i for i in s if i.isalpha()]
print(l)
    

print(20*37)

def facto(num:int):
    
