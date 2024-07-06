def count_factor(num:int):
    count=0
    i=1
    while i<=num:
        if num%i==0:
            count+=1
        i+=1
    return count

def prime_check(count):
    if count==2:
        return True
    return False

x=count_factor(4)
print(prime_check(x))