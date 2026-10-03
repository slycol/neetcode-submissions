class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)):
            j = i
            while j < len(prices):
                if (prices[j]-prices[i]>max):
                    max = prices[j]-prices[i]
                j+=1
        return max