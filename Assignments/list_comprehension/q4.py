l=[i for i in range(1,11)]
def exchange(lst:list):
    lst[0],lst[-1]=lst[-1],lst[0]
    print(lst)

exchange(l)