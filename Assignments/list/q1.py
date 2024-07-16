l=[4,8,6,5,3,12,1,3,19,2,14]

def oddCounter(lst:list)->int:
    count=0
    for numbers in lst:
        if numbers%2!=0:
            count+=1
    return count
def oddEvenCounter(lst:list):
    count=0
    even=0
    for numbers in lst:
        if numbers%2!=0:
            count+=1
        else:
            even+=1
    return count, even

odd=oddCounter(l)
count=oddEvenCounter(l)
od=count[0]
even=count[-1]
print("odd=",odd)
print(f"odd={od}\neven={even}")

