my_str="aaaabbbbbccccddddd"

def removeDublicate(s:str)->str:
    result=""
    for ch in s:
        if ch not in result:
            result+=ch
    return result
print(removeDublicate(my_str))