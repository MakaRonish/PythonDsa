def remove_vowels(word:str)->tuple:
    result=""
    result2=""
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    vowel="aeiouAEIOU"
    for ch in word:
        if ch not in vowels:
            result+=ch
    
    
    for ch in word:
        if ch not in vowel:
            result2+=ch
    return result2,result

print(remove_vowels("ROnish12345aeioutgyhb"))