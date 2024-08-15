def fibonacci(num:int):
    if num < 0:
        return "Invalid number"
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)
print(fibonacci(30))
#time complex==2^n