from cmath import cos
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)  # the top step cost

        # traverse from the top, minimal cost at the top is 0, 
        # and minimal cost at the step below the top is cost[-2] (the last one of original cost)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2]) # update i step minimal cost to the top

        return min(cost[0], cost[1])


class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.min_cost(cost, len(cost) - 1), self.min_cost(cost, len(cost) - 2))

    def min_cost(self, cost: List[int], i: int) -> int:
        if i == 0 or i == 1:
            return cost[i]

        return cost[i] + min(self.min_cost(cost, i - 1), self.min_cost(cost, i - 2))


s = Solution2()
cost = [10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]
print(s.minCostClimbingStairs(cost))