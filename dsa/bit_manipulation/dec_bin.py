def dec_bin(n: int) -> int:
    ans = ""
    while n > 0:
        rem = n % 2
        ans += str(rem)
        n = n // 2

    return int(ans[::-1])


def dec_bin1(n: int) -> int:
    ans = ""
    while n > 0:
        if n % 2 == 1:
            ans += "1"
        else:
            ans += "0"
        n = n // 2

    return int(ans[::-1])


print(dec_bin1(10))
