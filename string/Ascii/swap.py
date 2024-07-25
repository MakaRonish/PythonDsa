mystring="abcd123!@#  ABC"

def swap(word:str)->str:
    result=""
    for ch in word:
        ascii=ord(ch)
        if ascii>=65 and ascii<=90:
            result+=chr(ascii+32)
        elif ascii>=97 and ascii<=122:
            result+=chr(ascii-32)
        else:
            result+=ch
    return result

print(swap(mystring))

