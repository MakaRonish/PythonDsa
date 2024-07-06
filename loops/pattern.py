def pattern(num:int):
    i=1
    j=1
    while i<=num:
        while j<=i:
            print("*",end=" ")
            j+=1
        print("")
        i+=1
        j=1
pattern(5)

# better

def pattern1(n:int)->None:
    i=1
    num=1
    while i<=n:
        print(num)
        num=(num*10)+1
        i+=1
pattern1(10)