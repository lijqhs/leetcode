## 39. [Combination Sum](https://leetcode.com/problems/combination-sum/)

### Problem

Given an array of **distinct** integers `candidates` and a target integer `target`, return a list of all ***unique combinations*** of `candidates` where the chosen numbers sum to `target`. You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

#### Example 1:

    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.

### Solution

The idea of a solution is to find a path in which each number adds to the target. All we need is to find all the distinct paths.

```python
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        all = set()
        self.traverse(candidates, target, path, all)
        return [list(i) for i in all]


    def traverse(self, candidates: List[int], target: int, path: List[int], all: set) -> List[List[int]]:
        for n in candidates:
            new_path = [i for i in path]
            new_path.append(n)

            if target - n == 0:
                all.add(tuple(sorted(new_path)))
            elif target - n > 0:
                self.traverse(candidates, target-n, new_path, all)
            else:
                continue
```