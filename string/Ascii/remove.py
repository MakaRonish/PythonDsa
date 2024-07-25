mystring="123456RONish!@#$%^&*()"
def remove(string:str)->str:
    result=""
    for ch in string:
        if ("a"<=ch<="z") or ("A"<=ch<="Z"):
            result+=ch
    return result
print(remove(mystring))