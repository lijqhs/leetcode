
from typing import List
from collections import defaultdict, OrderedDict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for i in nums:
            d[i] += 1

        return list(dict(sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]).keys())


class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for i in nums:
            d[i] += 1

        return list(OrderedDict(sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]).keys())


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        f = [[] for i in range(len(nums))]

        for n in nums:
            d[n] += 1

        for n, c in d.items():
            f[c-1].append(n)

        output = []
        for i in range(len(f) - 1, -1, -1):
            for n in f[i]:
                output.append(n)
                if len(output) == k:
                    return output



nums = [1,1,1,2,2,3]
# nums = [1,2]
# nums = [1]
k = 2

s = Solution1()
print(s.topKFrequent(nums, k))
        