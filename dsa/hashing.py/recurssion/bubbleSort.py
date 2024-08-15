l=[8,2,1,4,6,5,9,3,7,-9,-100]

def bubble(l:list,i=0):
    n=len(l)
    for e in range(len(l)):
        swap=False  
        for j in range(0,n):
            print(j)
            if j+1==len(l):
             break   
            elif l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                swap==True
            elif swap==False:
               return l
            
        n=n-1
    return l
def bubble_rev(l:list):
    n=len(l)-1
    for j in range(len(l)):
        for k in range(n,-1,-1):
            if k==0:
                break
            elif l[k]>l[k-1]:
                l[k],l[k-1]=l[k-1],l[k]
    return l


    


    

print(bubble_rev([1,2,3,4,5]))

        

    