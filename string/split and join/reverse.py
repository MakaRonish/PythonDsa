my_str = "pyhton is good language"


def reverse(s: str):
    words = s.split(" ")
    result = ""
    for i in words:
        result += i[::-1]
        result+=" "
    result2=" ".join(i[::-1] for i in words)
    print(result)
    print(result2)
    words=words[::-1]
    new=" ".join(words)
    print(new)




reverse(my_str)

def re(s:str):
    words=s.split()
    words=words[::-1]
    result=" ".join(word[::-1] for word in words)
    return result

print(re(my_str))


my_list=[2,3,4,5,7,6,2,3]
print("-".join(str(i) for i in sorted(my_list)))
my_list.sort()
print(my_list)
