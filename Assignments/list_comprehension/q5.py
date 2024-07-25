lst=[i for i in range(20,36)]
def half(lst:list):
    n=len(lst)
    first=lst[:n//2]
    second=lst[n//2:]
    print(first)
    print(second)

half(lst)