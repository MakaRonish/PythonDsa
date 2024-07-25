my_str="qwertyui12345asdfgqwert1234sdfg345!@#$%^&"

def removenonalpha(s:str)->str:
    result=""
    for ch in s:
        if "a"<=ch<="z" or "A"<=ch<="Z" or ch==" ":
            result+=ch
    return result   

print(removenonalpha(my_str))