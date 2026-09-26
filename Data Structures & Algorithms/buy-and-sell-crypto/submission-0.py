class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_day, highest_day, highest_profit = 0, 0, 0
        for i in range(1, len(prices)):
            potential_profit = prices[i] - prices[lowest_day]
            highest_profit = max(highest_profit, potential_profit)
            lowest_day = i if prices[i] < prices[lowest_day] else lowest_day
        return max(0, highest_profit)
            