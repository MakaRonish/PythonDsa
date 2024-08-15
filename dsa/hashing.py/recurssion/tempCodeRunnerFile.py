def inser(l:list):
    for i in range(1,len(l)):
        if l[i]<l[i-1]:
            j=i-1
            n=j
            key=l[i]
            l[i]=l[j]
            for k in range(j,-1,-1):
                n-=1
                if l[k]>key:
                    l[k+1]=l[k]
                else:
                    break
            l[n+1]=key
    return l
print(inser([9,8,7,6]))