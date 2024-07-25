mystr="asdfgASDFG"


def upper(string:str)->str:
    result=""
    for ch in string:
        if "a"<=ch<="z":
            upper=chr(ord(ch)-32)
            print(upper)
            result+=upper
        else:
            result+=ch
    return result
print(upper(mystr))