my_str="sd1234 fg23sdfgh45sdfg67"
def digitCount(s:str)->int:
    c=0
    for ch in s:
        if "0"<=ch<="9":
            c+=1
    return c
print(digitCount(my_str))

