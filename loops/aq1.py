def multiply(num:int):
    product=1
    i=1
    while i<=num:
        product*=i
        i+=1
    return product
print(multiply(10))