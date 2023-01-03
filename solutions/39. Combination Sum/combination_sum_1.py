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



s = Solution()
c = [2,3,6,7]
t = 7

c = [2,3,5]
t = 8

# c = [8,7,4,3]
# t = 11

# c = [7,3,2]
# t = 18
all = s.combinationSum(c, t)
print(all)