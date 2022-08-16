## [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

>You are given an array `prices` where `prices[i]` is the price of a given stock on the ith day.
>
>You want to maximize your profit by choosing a **single day** to buy one stock and **choosing a different day in the future** to sell that stock.
>
>Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Key ideas:
- buy at i, sell at j
- each `price[j]` bigger than `price[i]` is a potential best sell price, record the biggest profit (`prices[j]-prices[i]`)
- each `price[j]` smaller than `price[i]` is a new buy price, reset i to j
- iterate `j` to find best sell price, by the way, find a good buy price

```python
from typing import List

class Solution:
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
```