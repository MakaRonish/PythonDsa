def func(n: int, count=0):
    print(count)
    count += 1
    if count == n:
        return
    func(n, count)


func(10)


def printName(n: int, c=1):

    name = "Ronish"
    print(c, name)
    c += 1
    if c > n:
        return
    printName(n, c)


printName(10)


def number(n: int, i=1):
    if i > n:
        return
    print(i)
    number(n, i + 1)


number(10)


def reverse(n: int, i=1):
    if n < i:
        return
    print(n)
    reverse(n - 1, i)
    print(f"{n} going back")
    n+=1


reverse(10)

def recur_without_plus(n:int):
    if n<1:
        return
    recur_without_plus(n-1)
    print(n)
recur_without_plus(10)

def backtrack(n:int,i=1)->None:
    if i>n:
        return
    backtrack(n,i+1)
    print(i,end="-")
backtrack(10)

   
    #Complete this function
def printNos(N):
    #Your code here
    if N<1:
        return
    printNos(N-1)
    print(N)

printNos(10)


