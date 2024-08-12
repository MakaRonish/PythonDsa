import math
num = 123
num_of_digit=int(math.log10(num))+1
print(num_of_digit)

reverse = 0
while num > 0:
    c = 1
    last_digit = num % 10
    num = num // 10
    reverse = reverse * 10 + last_digit

print(reverse)


def reverse_digit(num:int)->int:
    if num<0:
        x=-1*num
        sign=-1
    else:
        x=num
        sign=1
    revers=0
    while x>0:
        revers=revers*10+x%10
        x=x//10
    return revers*sign
print(reverse_digit(-987654))






