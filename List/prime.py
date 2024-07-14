l=[1,2,3,4,5,6,7,8,9,10,11]
def divisible(num:int)->int:
    count=0
    while True:
        for number in range(1,num+1):
            if num%number==0:
                count+=1
        break
    return count


def primeprinter(lst:list)->None:
    for item in lst:
        if divisible(item)==2 or divisible(item)==1:
            print(item)


primeprinter(l)