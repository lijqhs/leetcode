from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        all = []
        self.traverse(candidates, target, path, all)
        return all

    def traverse(self, candidates: List[int], target: int, path: List[int], all: set) -> List[List[int]]:
        if target == 0:
            all.append(path)
            return
        if target < 0:
            return

        for i, n in enumerate(candidates):
            self.traverse(candidates[i:], target-n, path+[n], all)


import time
t0 = time.perf_counter()

s = Solution()
c = [2,3,6,7]
t = 7

c = [2,3,5]
t = 8

c = [8,7,4,3]
t = 11

# c = [7,3,2]
# t = 18
all = s.combinationSum(c, t)
print(all)

elapsed = time.perf_counter() - t0
print(f'{elapsed:0.8f}s')