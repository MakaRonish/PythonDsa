def stronly(dic:dict):
    new={}
    for key,items in dic.items():
        if isinstance(items,str):
            new[key]=items
    print(new)

dic={"1":"a","2":2,"3":4,"5":"5"}
stronly(dic)