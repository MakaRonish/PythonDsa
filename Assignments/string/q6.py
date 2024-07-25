my_str="rn"


# def capitalize(s:str)->str:
#     c=1
#     wordtocap=True
#     if "a"<=s[0]<="z":
#         result=chr(ord(s[0])-32)
#     else:
#         result=s[0]
#     for ch in range(1,len(s)):
#         c+=1
#         if wordtocap:
#             if "a"<=s[ch+1]<="z":
#                 result+=" "
#                 result+=chr(ord(s[c])-32)
#             else:
#                 result+=" "
#                 result+=s[c]
#         if s[ch]==" ":
#             # if "a"<=s[ch+1]<="z":
#             #     result+=" "
#             #     result+=chr(ord(s[c])-32)
#             # else:
#             #     result+=" "
#             #     result+=s[c]
#             wordtocap=True
#         else:
#             result+=s[ch]
#     return result

# print(capitalize("my name is ronish"))


my_str="My name is Ronish"

def capitalizer(s:str)->str:
    result=""
    next_to_cap=True
    for ch in s:
        if next_to_cap:
            if "a"<=ch<="z":
                result+=chr(ord(ch)-32)
                next_to_cap=False
            else:
                result+=ch
                next_to_cap=False
        else:
                result+=ch

        if ch==" ":
            next_to_cap=True
            
    return result

print(capitalizer(my_str))


def capitalize(s: str) -> str:
    result = ""
    is_new_word = True
    for char in s:
        if is_new_word and "a" <= char <= "z":
            result += chr(ord(char) - 32)
            is_new_word = False
        else:
            result += char
            is_new_word = False
        if char == " ":
            is_new_word = True
    return result

print(capitalize(my_str))


            
        
        