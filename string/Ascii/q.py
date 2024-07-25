mystring="12345"
def lower(strin:str):
    c=0
    for chr in mystring:
        if "A"<=chr<="Z":
            return False
        elif "a"<=chr<="z":
            c+=1
    if c>0:
        return True
    return False
        
print(lower(mystring))