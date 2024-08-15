def sumOfDivisors(N):
    #code here
    total=0
    for i in range(N):
        sum=0
        for j in range(1,i+1):
            if i%j==0:
                sum+=j
        total+=sum
        
    return total

print(sumOfDivisors(4))


print(5//2)