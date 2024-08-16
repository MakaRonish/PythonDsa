def reverse(word:str,i=0)->str:
    if i==len(word)-1:
        return word[i]
    return reverse(word,i+1) + word[i]


print(reverse("geekforgeek"))
