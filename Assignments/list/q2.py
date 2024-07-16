l = [4, 8, 6, 5, 3, 12, 1, 7, 6, 2]


def prime(lst: list):
    total=0
    for number in lst:
        count = 1
        if number==1:
            print(number)
            total+=number
            continue
        for indec in range(1, number // 2 + 1):
            if number % indec == 0:
                count += 1
        if count == 2:
            print(number)
            total+=number
        
    print("the total of prime number is",total)

prime(l)

