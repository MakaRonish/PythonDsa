l=[1,2,3,4,5,6,7,8,1,2,3,3,2,1,2,2,3,4,3,2,2,1,2,4,2,1,2]
my_dic={}
for num in l:
    my_dic[num]=my_dic.get(num,0)+1

max=float("-inf")
min=float("inf")
maxEle=""
minEle=""
for key,values in my_dic.items():
    if values > max:
        max=values
        maxEle=key
    if values<min:
        min=values
        minEle=key
print(maxEle,max)
print(minEle,min)

