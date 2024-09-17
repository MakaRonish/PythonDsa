def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    str_num = str(x)
    reversenum = int(str_num[::-1])
    if reversenum > 2147483647 or reversenum < -2147483648:
        return 0
    return reversenum


print(reverse(56789))