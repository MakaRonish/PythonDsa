l=[]
def prime(n:int):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
def listofprime(end:int):
    l=[i for i in range(1,end+1) if prime(i)]
    print(l)

listofprime(20)


print(15%3)