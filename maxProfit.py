class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        lowprice = prices[0]
        sumprofit = 0
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] >= prices[i-1]:
                profit = prices[i] - lowprice
                if i == len(prices)-1:
                    profit = prices[i]-lowprice
                    sumprofit += profit
            else:
                profit = prices[i-1]-lowprice
                lowprice = prices[i]
                sumprofit += profit                
        return sumprofit

    
    
    
    #更简单的方法：
    class Solution:
    def maxProfit(self, prices) -> int:
        sumprofit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]: #把所有增量累加起来
                sumprofit += prices[i] - prices[i-1]
        return sumprofit
