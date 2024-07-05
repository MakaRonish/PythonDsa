def addofevennumbers(start:int,end:int):
    i=start
    sum=0
    while i<=end:
        if i%2==0:
            sum+=i
        i+=1
    print(sum)
addofevennumbers(10,20)
