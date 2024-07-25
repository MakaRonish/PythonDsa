def upper(word:str)->str:
    result=""
    for ch in word:
        ascii=ord(ch)
        if ascii>=97 and ascii<=122:
            ascii-=32
            result+=chr(ascii)
            print(result)
        else:
            result+=ch
    return result

print(upper("qwertyuiop123456789!@#$%^&*"))
