# def startend(start:int,end:int):
#     while start<=end:
#         print(start,end=" ")
#         start+=1


#usually dont change the input 


def startend(start:int,end:int):
    while start<=end:
        start+=1
        return start
        
start=int(input("start:"))
end=int(input("ENd:"))

startend(start,end)