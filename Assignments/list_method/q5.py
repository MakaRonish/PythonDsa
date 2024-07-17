l=[34,56,78,10,20,44]

def removing(l:list,n:int):
    if n>len(l) or n<-len(l):
        print("index doesnt exist")
    else:
        l.pop(n)
        print(l)
n=int(input('num='))
removing(l,n)

