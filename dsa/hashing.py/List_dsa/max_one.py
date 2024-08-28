def max_one(arr):
    one_max=0
    c=0
    for i in arr:
        if i==1:
            c+=1
        else:
            if one_max<c:
                one_max=c
            c=0
    if c>one_max:
        one_max=c

    return one_max


print(max_one([1,0,1,1,0,1]))




