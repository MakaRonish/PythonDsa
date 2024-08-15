def sum1(i,sum):
    if i<1:
        print(sum)
        return 
    sum1(i-1,sum+i)
sum1(5,0)