dic1={"a":1,'b':2,'c':'c','d':9}
def remove(dic1,k):
    result={}
    for key,value in dic1.items():
        
        if isinstance(value,str) or value<=k:
            result[key]=value
            
       
    print(result)
remove(dic1,0)
