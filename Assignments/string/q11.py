my_str="as dfg"
def check(s:str)->bool:
    for ch in s:
        if not(("a"<=ch<="z" or "A"<=ch<="Z") or ch==" "):
            return False
    return True

print(check(my_str))