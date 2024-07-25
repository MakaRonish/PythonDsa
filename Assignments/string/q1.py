def reverse_string(word:str)->str:
    result=word[::-1]
    return result
word=input("Enter a string:")
print(reverse_string(word))