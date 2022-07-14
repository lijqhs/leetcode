from cmath import cos
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)  # the top step cost

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2]) # update i step minimal cost to the top

        return min(cost[0], cost[1])


class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c = cost
        c.append(0)

        for i in range(len(c) - 3, -1, -1):
            c[i] += min(c[i + 1], c[i + 2]) # update minimal cost of step i to the top

        return min(c[0], c[1])


class Solution2:
    """
    recursive solution
    error: Time Limit Exceeded
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.min_cost(cost, len(cost) - 1), self.min_cost(cost, len(cost) - 2))

    def min_cost(self, cost: List[int], i: int) -> int:
        if i == 0 or i == 1:
            return cost[i]

        return cost[i] + min(self.min_cost(cost, i - 1), self.min_cost(cost, i - 2))



class Solution3:
    """
    recursive solution with memoization
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        recursive solution with memoization
        """
        c = [0] * len(cost)
        return min(self.min_cost(cost, len(cost) - 1, c), self.min_cost(cost, len(cost) - 2, c))

    def min_cost(self, cost: List[int], i: int, c: List[int]) -> int:
        if i == 0 or i == 1:
            return cost[i]

        if c[i] != 0: return c[i]

        c[i] = cost[i] + min(self.min_cost(cost, i - 1, c), self.min_cost(cost, i - 2, c))

        return c[i]



class Solution4:
    """
    bottom-up solution
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        bottom-up solution
        """
        c = [0] * len(cost)
        for i in range(len(cost)):
            if i < 2: 
                c[i] = cost[i]
            else:
                c[i] = cost[i] + min(c[i - 1], c[i - 2])

        return min(c[len(cost) - 1], c[len(cost) - 2])

class Solution5:
    """
    bottom-up solution, optimization of space
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        bottom-up solution, optimization of space
        """
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])

        return min(cost[len(cost) - 1], cost[len(cost) - 2])


s = Solution1()
cost = [10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]
print(s.minCostClimbingStairs(cost))