from typing import List

class Solution:
    """
    Bad: Time Limit Exceeded (for large decreasing arrays)
    """
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maxProfit = max(maxProfit, prices[j]-prices[i])

        return maxProfit


class Solution1:
    """
    Bad: Time Limit Exceeded
    """
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        i = 0
        while i < len(prices):
            while i<len(prices)-1 and prices[i] >= prices[i+1]:
                i += 1
            # ii = i
            for j in range(i+1, len(prices)):
                if prices[j]-prices[i] > maxProfit:
                    maxProfit = prices[j]-prices[i]
            
            i += 1
            #     if prices[j] < prices[ii]:
            #         ii = j
            # i = ii

        return maxProfit


class Solution2:
    """
    Finally, accepted! Thanks god.
    """
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        i = 0
        while i < len(prices):
            while i < len(prices)-1 and prices[i] >= prices[i+1]:
                i += 1

            new_i = i   # to find a smaller one to update i

            for j in range(i+1, len(prices)):
                if prices[j]-prices[i] > maxProfit:
                    maxProfit = prices[j]-prices[i]
            
                if new_i == i and prices[j] < prices[new_i]:
                    new_i = j
                    break

            if i == new_i: i += 1
            else: i = new_i

        return maxProfit


class Solution3:
    """
    Revised 
    """
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        i, j = 0, 1
        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
            else:
                maxProfit = max(prices[j]-prices[i], maxProfit)
            j += 1

        return maxProfit



prices = [7,1,5,3,6,4]
prices = [7,1,5,0,3,6,4,0,4]
s = Solution3()
print(s.maxProfit(prices))
