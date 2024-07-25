# my_string = "one twoo three"

# def longest_word(s: str) -> str:
#     result = ""
#     longest = ""
#     lenght=len(s)
#     c=0
#     for i in s:
#         c+=1
#         if i!=" ":
#             result += i
#         if i == " " or lenght==c:
#             if c == lenght and i != " ":  
#                 result += i
#             if len(longest) < len(result):
#                 longest = result
#             result=""

#     return longest


# print(longest_word(my_string))


my_string = "python is a very easy coding language to learn"


def longest_word(s: str) -> str:
    result = ""
    longest = ""
    lenght=len(s)
    c=0
    for i in s:
        c+=1
        if i!=" ":
            result += i
        if i == " " or lenght==c:
            if len(longest) < len(result):
                longest = result
                result=""
            else:
                result=""
    return longest


print(longest_word(my_string))
