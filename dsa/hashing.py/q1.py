def string_counter(list:list,word:str)->list:
    hash_map={}
    l=[]
    for chr in word:
        hash_map[chr]=hash_map.get(chr,0)+1
    for chr in list:
        a=hash_map.get(chr,0)
        l.append(a)
    return l


print(string_counter(["a","b","c","z","x"],"abcacbacbaaa"))

def string_counter2(list:list,word:str)->list:

    l=[0]*26
    ans=[]
    for chr in word:
        asci=ord(chr)
        if asci<91:
            l[asci-65]+=1
        else:
            l[asci-97]+=1

    for chr in list:
        ascii=ord(chr)
        if ascii<91:
            ans.append(l[ascii-65])
        else:
            ans.append(l[ascii-97])
        
    return ans

print(string_counter2(["a","b"],"aabbA"))