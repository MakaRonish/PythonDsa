def insertion_sort(l:list):
    for i in range(1,len(l)):
        if l[i]<l[i-1]:
            j=i-1
            key=l[i]
            for k in range(j,-1,-1):
                if l[k]>key:
                    l[k+1]=l[k]
                elif l[k]<key:
                    l[k+1]=key

    return l

print(insertion_sort([1,9,8,7]))


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


#correct way 
#time comple
def insert(l:list):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and l[j]>key:
            l[j+1]=l[j]
            j-=1
        l[j+1]=key
    return l
print(insert([9,8,7,6,5,4]))





            



                



                



