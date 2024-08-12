def palindrome(num: int):
    x = num
    reverse = 0
    while x > 0:
        reverse = reverse * 10 + x % 10
        x = x // 10
    return reverse == num


print(palindrome(121))
print(palindrome(12345))
print(palindrome(123454321))


def str_palindrome(word: str):
    s = word
    revers = ""
    for ch in range(len(s)-1, -1, -1):
        revers += s[ch]
    return revers


print(str_palindrome("Ronish"))
print(str_palindrome("Mommy"))
print(str_palindrome("priya"))
