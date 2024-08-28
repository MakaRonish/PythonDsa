class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        a=0
        b=0
        result=[]
        while True:
            if a>=n and b>=m:
                break
            if arr1[a]<arr2[b]:
                result.append(arr1[a])
                a+=1
            elif arr1[a]>arr2[b]:
                result.append(arr2[b])
                b+=1
            else:
                result.append(arr1[a])
                a+=1
            

            if a>=n:
                while b<m:
                    result.append(arr2[b])
                    b+=1
            if b>=m:
                while a<n:
                    result.append(arr1[a])
                    a+=1
        return result
    def Union_2(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        a=0
        b=0
        result=[]
        while True:
            if a>=n and b>=m:
                break
            if arr1[a]<arr2[b]:
                result.append(arr1[a])
                a+=1
            elif arr1[a]>arr2[b]:
                result.append(arr2[b])
                b+=1
            else:
                result.append(arr1[a])
                a+=1
            

            if a>=n:
                while b<m:
                    result.append(arr2[b])
                    b+=1
            if b>=m:
                while a<n:
                    result.append(arr1[a])
                    a+=1
        return result
    
    def Union(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        a=0
        b=0
        result=[]
        while True:
            if a>=n and b>=m:
                break
            if arr1[a]<arr2[b]:
                if arr1[a] not in result:
                    result.append(arr1[a])
                    a+=1
                else:
                    a+=1
            elif arr1[a]>arr2[b]:
                if arr2[b] not in result:
                    result.append(arr2[b])
                    b+=1
                else:
                    b+=1
            else:
                if arr1[a] not in result:
                    result.append(arr1[a])
                    a+=1
                else:
                    a+=1
            

            if a>=n:
                while b<m:
                    if arr2[b] not in result:
                        result.append(arr2[b])
                        b+=1
                    else:
                        b+=1
            if b>=m:
                while a<n:
                    if arr1[a] not in result:
                        result.append(arr1[a])
                        a+=1
                    else:
                        a+=1
        return result
            
#time complexity too much for union



a=Solution()
print(a.findUnion([1,2,3,4,5],[2,4,6,8,10],5,5))
print(a.Union([1,2,3,4,5,1,2,3,4,5],[2,4,6,8,10],5,5))


def Union(arr1,arr2):
    result=[]
    pointer_1=0
    pointer_2=0
    size=len(arr1)
    while pointer_1<size or pointer_2<size:
        if arr1[pointer_1]<arr2[pointer_2]:
            if len(result)==0:
                result.append(arr1[pointer_1])
                pointer_1+=1
            elif result[-1]>=arr1[pointer_1]:
                pointer_1+=1
            else:
                result.append(arr1[pointer_1])
                pointer_1+=1
        elif arr1[pointer_1]>arr2[pointer_2]:
            if len(result)==0:
                result.append(arr2[pointer_2])
                pointer_2+=1
            elif result[-1]>=arr2[pointer_2]:
                pointer_2+=1
            else:
                result.append(arr2[pointer_2])
                pointer_2+=1
        else:
            if len(result)==0:
                result.append(arr2[pointer_2])
                pointer_2+=1
            elif result[-1]>=arr2[pointer_2]:
                pointer_2+=1
            else:
                result.append(arr2[pointer_2])
                pointer_2+=1
        if pointer_1>=size-1:
            while pointer_2<=size-1:
                if result[-1]<arr2[pointer_2]:
                    result.append(arr2[pointer_2])
                    pointer_2+=1
                else:
                    pointer_2+=1
        if pointer_2>=size-1:
            while pointer_1<=size-1:
                if result[-1]<arr1[pointer_1]:
                    result.append(arr1[pointer_1])
                    pointer_1+=1
                else:
                    pointer_1+=1

        return result
    
print(Union([1,2,3,4,5],[1,2,3,4,5]))

        





            

