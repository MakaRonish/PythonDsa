import math
def num_of_digit(n:int):
    a=n
    return int(math.log10(n))+1


def armstrong(num: int) -> int:
    x = num
    c=num_of_digit(num)
    total = 0
    while x > 0:
        lastdigit = x % 10
        x = x // 10
        total += lastdigit**c
    return total == num


print(armstrong(1))



class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        factor_A=[A]
        factor_B=[B]
        for i in range(2,A):
            if A%i==0:
                factor_A.append(i)
        for i in range(2,B):
            if B%i==0:
                factor_B.append(i)
            
        factor=[value for value in factor_A if value in factor_B]
        if len(factor)==0:
            GCD=1
        else:
            GCD=max(factor)
        LCM=(A*B)/GCD
        return [int(LCM),int(GCD)]
