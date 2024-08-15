def reverse(word: str, i=0):
    if i == len(word) - 1:
        return word[i]
    else:
        return reverse(word, i + 1) + word[i]


print(reverse("ronish"))
n = []


def revlist(list, i=0):
    if i == len(list) - 1:
        n.append(list[i])
        return
    revlist(list, i + 1)
    n.append(list[i])
    return n


print(revlist([1, 2, 3, 4]))
l = [1, 2, 3,4,5,6]


def re(list, start=0, end=len(l) - 1):
    if start > end:
        return
    l[start],l[end]=l[end],l[start]
    re(list, start + 1, end - 1)


re(l)
print(l)

def factorialNumbers(n):
    	#code here
    li=[]
    for i in range(1,n+1):
        fac=i
        for j in range(i-1,0,-1):
            fac*=j
        if fac>n:
            break
        li.append(fac)
    print(li)
    for i in li:
        print(i,end=" ")
factorialNumbers(3)
