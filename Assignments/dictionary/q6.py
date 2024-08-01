dic={
    "a":3,"b":"hello","c":7.5,"d":10
    }
print(type("a"))
def fac(dic,factor:int):
    for i,j in dic.items():
        if type(j)!=str:
            dic[i]=j*factor
           
        
fac(dic,2)
print(dic)

