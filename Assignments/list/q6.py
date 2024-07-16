l=[4, 8, 6, 19, 3, 12, 1, 7, 6, 2]
def largestPrime(l:list):
    max=0
    for i in l:
        count=1
        for j in range(1,i//2+1):
            if i%j==0:
                count+=1
        if count==2:
            if i>max:
                max=i
    print(max)

largestPrime(l)


            
    