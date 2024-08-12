le=[]
nu=[]
def factorial(n: int) -> int:
    nu.append(n)
    if n == 1:
        le.append(1)
        return 1
    fac= n * factorial(n - 1)
    if fac<=max(nu):
        le.append(fac)
    return fac

print(factorial(10))
print(le)