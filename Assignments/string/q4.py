def wordcount(word:str)->int:
    c=1
    if not word:
        return 0
    for ch in word:
        ascii=ord(ch)
        if ascii==32:
            c+=1
    return c

word=""
count=wordcount(word)
print("number of word is",count)
        
    