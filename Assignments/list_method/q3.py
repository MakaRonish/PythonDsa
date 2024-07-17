def inputtake(length:int)->tuple:
    l=[]
    result=[]
    for i in range(length):
        element=int(input(f"Enter element{i+1}="))
        l.append(element)
    
    for elements in l:
        if elements%2!=0:
            result.append(elements)
    return l , result
length=int(input("length:"))
ans=inputtake(length)
print(f"list = {ans[0]}\n remove even={ans[-1]}")