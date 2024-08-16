def GCD(num1:int,num2:int)->int:
    if num1==0:
        return num2
    elif num2==0:
        return num1
    if num1>num2:
        return GCD(num2,num1-num2)
    else:
        return GCD(num2-num1,num1)
    
print(GCD(270,192))

def GCD2(num1: int, num2: int) -> int:
    if num2 == 0:
        return num1
    else:
        return GCD2(num2, num1 % num2)

print(GCD2(192, 270))


print(192%192)