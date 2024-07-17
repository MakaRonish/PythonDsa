l=[1,2,3,4,5,6,7,8,9,10,11,12]
def even_odd(l:list):
    even=[]
    odd=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print(f"even={even}\nodd={odd}")

even_odd(l)
