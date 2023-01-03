from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        all = set()
        candidates = sorted(candidates)
        self.traverse(candidates, target, path, all)
        return [list(i) for i in all]


    def traverse(self, candidates: List[int], target: int, path: List[int], all: set) -> List[List[int]]:
        for n in candidates:
            path.append(n)

            if target - n == 0:
                all.add(tuple(sorted(path)))
                path.pop()
            elif target - n > 0:
                self.traverse(candidates, target-n, path, all)
                path.pop()
            else:
                path.pop()
                break


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