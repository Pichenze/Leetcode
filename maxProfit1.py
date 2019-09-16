class Solution:
	def maxProfit(self, prices):
		minprice = 1e20
		maxprofit = 0
		for i in range(len(prices)):
			if prices[i] < minprice:
				minprice = prices[i]
			elif prices[i] - minprice > maxprofit:
				maxprofit = prices[i] - minprice
		return maxprofit