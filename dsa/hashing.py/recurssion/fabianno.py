# def fib( n):
#     """
#         :type n: int
#         :rtype: int
#         """
#     l=[0,1]
#     if n==1:
#         return l[0]
#     elif n==2:
#         return l[1]
#     else:
#         for i in range(n-2):
#             l.append(l[i]+l[i+1])
#     print(l)
#     return l[-1]

i=1
l=[0,1,2]
def fib2(n,i):
    """
        :type n: int
        :rtype: int
        """
    if n==0:
        return l[0]
    elif n==2 or n==1:
        return l[1]
    elif n==3:
        return l[2]
    else:
        if i==n-1:
            return
        else:
            l.append(l[i]+l[i+1])
            fib2(n,i+1)
    print(l)
    return l[-1]

print(fib2(5,i))

l=[1,2,3]

def lis(l=[1,2,3],i=1):
    if i==10:
        return
    l.append(i)
    lis(i=i+1)
    return l

print(lis())

class Example:
    l=[1,2,3]
    

    def gg(self,i=1):
        print(i)
        self.l.append(9)
        print(self.l)


a=Example()
a.gg()


