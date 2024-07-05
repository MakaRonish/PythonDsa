def div(num1,num2):
    count=0
    while num1<=num2:
        if num1%7==0:
            count+=1
        num1+=1
    print(count)

def div2(num1,num2):
    count=0
    while num1<=num2:
        if num1%7==0 and num1%2==0:
            count+=1
        num1+=1
    print(count)
div(5674,10983)
div2(5674,10983)