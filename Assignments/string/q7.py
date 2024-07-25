my_str="aAEFGHJKIOasdfghjklqwertyuiopzxcvbnm"

def removeCon(s:str)->str:
    vowels="aeiouAEIOU"
    result=""
    for ch in s:
        if ch not in vowels:
            result+="*"

        else:
            result+=ch
    return result

print(removeCon(my_str))
