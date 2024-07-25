mystr="a b c d w s d f h h"
def space(s:str)->str:
    result=""
    for ch in s:
        if ch==" ":
            result+="-"
        else:
            result+=ch
    return result

print(space(mystr))