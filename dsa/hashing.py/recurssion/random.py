# def sumOfSeries(n):
#         #code here
#         if n==1:
#             return 1
#         total= n**3 + sumOfSeries(n-1)
#         return total

# print(sumOfSeries(118991))
l=[]
def factorialNumbers(n):
    	#code here 
    if n==1:
        return 1
    num= n*factorialNumbers(n-1) 
    if num<=n:
        l.append(num)
    return num

(factorialNumbers(6))
print(l)



# l = []

# def factorialNumbers(n):
#     # Base case
#     if n == 1:
#         l.append(1)
#         return 1
    
#     # Recursive case
#     num = n * factorialNumbers(n - 1)
    
#     # Only append if the factorial is less than or equal to n
#     if num <= n:
#         l.append(num)
        
#     return num

# factorialNumbers(6)
# print(l)