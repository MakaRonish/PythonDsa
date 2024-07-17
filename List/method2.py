l=[1,2,3,4,"a",True]
print(l)
l.append("hello") #put at last
print(l)


#annotation
lst:list[int]=[1,2,3] #will still run even if the list is not int just for us

from typing import List

ls:List[int]=[1,2,3]
ls.append("a")
print(ls)

ls.insert(-20,3.5)
print(ls)

z=ls.pop()
print(z)

# ls.clear()

ls.extend([[90,100,1000]])
print(ls) 
