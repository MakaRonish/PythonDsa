le = []
nu = []


def factorial(n: int) -> int:
    nu.append(n)
    if n == 1:
        le.append(1)
        return 1
    fac = n * factorial(n - 1)
    if fac <= max(nu):
        le.append(fac)
    return fac


print(factorial(24))
print(le)


l = []


def factorialNumbers(n):
    if n == 1:
        l.append(1)
        return 1
    num = n * factorialNumbers(n - 1)
    if num <= n:
        l.append(num)
    return num


factorialNumbers(10)
print(l)


def count(n):
    x = n
    print(f"x:{x}")
    if n == 1:
        return
    count(n - 1)
    print(n)


count(5)
