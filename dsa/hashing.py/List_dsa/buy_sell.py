# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """

#         buy=None
#         buy_amount=float("inf")
#         sell=0
#         pro=0
#         for i in range(len(prices)):
#             if prices[i]<buy_amount:
#                 buy=i
#                 buy_amount=prices[i]
#         for i in range(buy+1,len(prices)):
#             profit=prices[i]-buy_amount
#             if profit>pro:
#                 sell=i
#                 pro=profit
#         if pro==0:
#             print("0")
#         else:
#             print(f"buy={buy}\nsell={sell}\nprofit={pro}")
# a=Solution()
# a.maxProfit([1,2])

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i]>profit:
                    profit=prices[j]-prices[i]
        return profit
                
    def trying_(self,prices):
        pointer=0
        buy=0
        buy_amount=prices[buy]
        sell=None
        sell_amount=None
        total_profit=0
        while pointer<len(prices)-1:
            pointer+=1
            if prices[pointer]>prices[buy]:
                sell=pointer
                sell_amount=prices[sell]
                profit=sell_amount-buy_amount
                if total_profit<profit:
                    total_profit=profit
                    
                    b=buy
                    s=sell

                
            elif prices[pointer]<prices[buy]:
                buy=pointer
                buy_amount=prices[buy]

        print(b)
        print(s)

        return total_profit
                

                
            


a=Solution()
print(a.trying_([7,1,5,3,6,4]))
