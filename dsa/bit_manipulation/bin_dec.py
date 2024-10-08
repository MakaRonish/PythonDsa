def bin_dec(n):
    dec = 0
    j = 0
    for i in range(len(n) - 1, -1, -1):
        dec += int(n[j]) * (2**i)
        j += 1
    return dec


print(bin_dec("0111"))
