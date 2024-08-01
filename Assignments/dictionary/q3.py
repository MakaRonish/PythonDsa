def join(l: list, l1: list):
    dic = {}
    for i in range(0, len(l)):
        dic[l[i]] = l1[i]
    return dic
def join2(l: list, l1: list):
    dic = {}
    for i,j in zip(l,l1):
        dic[i]=j
    return dic


l = ["1", "2", "3"]
l1 = ["a", "b", "c"]

print(join2(l, l1))
