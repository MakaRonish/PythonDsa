l=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

def freq(l:list):
    result={}
    for i in l:
        if i not in result:
            result[i]=1
        else:
            result[i]+=1
    return result

print(freq(l))

#faster

r={

}
for num in l:
    r[num]=r.get(num,0)+1
max=0
key=""
for num in r:
    if max<r[num]:
        max=r[num]
        key=num
print(key,max)
    


print(r)
