## [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

```python
from typing import List

class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        maxLen = 0 # longest length

        for n in nums:
            if n-1 in unique: # otherwise, time limit will exceed
                continue
            # n is a start of a sequence (at least itself)
            i = 1
            while n+i in unique:
                i += 1
            maxLen = max(maxLen, i)
        
        return maxLen
```

