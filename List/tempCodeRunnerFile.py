def divisible(num:int)->int:
    count=0
    while True:
        for number in range(1,num+1):
            if num%number==0:
                count+=1
        break
    return count
print(divisible(4))