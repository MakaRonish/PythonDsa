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
print(a.Union([1,2,3,4,5],[2,4,6,8,10],5,5))



            

