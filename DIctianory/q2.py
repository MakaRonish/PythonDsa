mystring="aaabbbcc"

def fre(str):
    result={}
    equal={}
    repfreq=0
    reqstr=""
    for i in str:
        result[i]=result.get(i,0)+1
    for key in result:
        if repfreq<result[key]:
            repfreq=result[key]
            reqstr=key
    for key,value in result.items():
        if repfreq==value:
            equal[key]=value
    print(reqstr)
    print(repfreq)
    print(equal)

fre(mystring)
