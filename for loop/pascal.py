def pascal(length:int)->None:
    l=[]
    pascal=[]
    
    for i in range(1,length+1):
        pascal.append(1)
        for j in range(len(l)):
            if j!=(len(l)-1):
                new_ele=l[j]+l[j+1]
                pascal.append(new_ele)
            else:
                pascal.append(1)
        for element in pascal:
            print(element,end=" ")
            print(" ",end=" ")
        print()
        l.clear()
        for i in pascal:
            l.append(i)
        pascal.clear()


pascal(5)

l=[1,1,1,1,1,1,2,2,2,2,3,3,3,3]
d={}
for i in l:
    d[i]=d.get(i,0)+1
print(d)

print(d[1])
k=[1 for i in range(10)]
print(k)
print()
a="-".join(str(k))
print(a)


class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        dic={}
        for i in arr:
            dic[i]=dic.get(i,0)+1
        for i in range(1,P+1):
            a=dic.get(i,0)
            print(a,end=" ")

s=Solution()
s.frequencyCount([2,3,2,3,5],5,5)


