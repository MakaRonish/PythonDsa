mystring="dhaw43789HGDSAK&*(#$  HDK486/*-+daw)"

def counters(words:str):
    alpha=0
    num=0
    space=0
    symbol=0
    for ch in words:
        ascii=ord(ch)
        if (ascii>=65 and ascii<=90) or (ascii>=97 and ascii<=122):
            alpha+=1
        elif ascii>=48 and ascii<=57:
            num+=1
        elif ascii==32:
            space+=1
        else:
            symbol+=1

    print(alpha)
    print(num)
    print(space)
    print(symbol)

counters(mystring)