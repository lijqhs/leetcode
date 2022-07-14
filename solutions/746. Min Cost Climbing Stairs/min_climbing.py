from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)  # the top step cost

        # traverse from the top, minimal cost at the top is 0, 
        # and minimal cost at the step below the top is cost[-2] (the last one of original cost)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2]) # update i step minimal cost to the top

        return min(cost[0], cost[1])


s = Solution()
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))