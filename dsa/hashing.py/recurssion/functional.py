def add(num:int)->int:
    if num==1:
        return 1
    return num + add(num-1)
print(add(10))

def reverse(word:str,i=0):
    if i==len(word)-1:
        return word[i]
    return reverse(word,i+1)+word[i]
print(reverse("edcba"))