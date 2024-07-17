# def asking(num:int)->list[int]:
#     l=[]
#     for number in range(1,num+1):
#         a=int(input("Enter a number:"))
#         l.append(a)
#     return l
# num=int(input("Enter a number"))
# x=asking(num)
# print(x)

#remove even

lis=[5,7,4,2,8,7,6,9,10,1,2]

def remove_even(l:list):
    new=[]
    for i in l:
        if i%2!=0:
            new.append(i)
    return new
    
        
    

print(lis)

he=remove_even(lis)
print(he)
