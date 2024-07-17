l=[3, 5, 3, 7, 3, 2, 5, 3, 5, 7, 2, 9, 5, 6, 5, 7, 8, 7, 7]

def printing(l:list):
    
    result=[]
    for i in l:
        count=l.count(i)
        if count>3 and i not in result:
            result.append(i)
    for i in result:
        print(i)
            
        
printing(l)

def counting(l):
    result=[]
    for i in l:
        c=0
        for index in range(len(l)):
            if i==l[index]:
                c+=1
        if c>3 and i not in result:
            result.append(i)

    print(result)


            

counting(l)