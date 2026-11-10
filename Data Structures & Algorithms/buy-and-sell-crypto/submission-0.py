class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        pt1 = 0
        pt2 = 1

        while pt2 < len(prices):
            if prices[pt1] < prices[pt2]:
                profit = prices[pt2] - prices[pt1]
                maxp = max(maxp, profit)
            else:
                pt1 = pt2
            pt2 += 1
        
        return maxp
