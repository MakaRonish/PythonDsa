my_list=[ i for i in range(1,11) if i%2==0]
print(my_list)


def prime_number(n:int)->bool:
    for i in range(2,n):
        if n%i!=0:
            return True
    return False

my_list=[ i for i in range(1,100) if prime_number(i)]
print(my_list)


lst=[f"{i}5 facotr" if i%5==0 else f"{i}not div by 5" for i in range(1,50)]
print(lst)