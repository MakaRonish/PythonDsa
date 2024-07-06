def factor_add(num:int)->int:
    i=1
    sum=0
    while i<=num:
        if num%i==0:
            sum+=i
        i+=1
    return sum
    
print(factor_add(10))