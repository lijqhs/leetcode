
from typing import List


class Solution1:
    """
    !!Bad: Time Limit Exceeded
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        maxLen = 0 # longest length

        for n in nums:
            i = 1
            while n+i in unique:
                i += 1
            maxLen = max(maxLen, i)
        
        return maxLen


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


nums = [0,3,7,2,5,8,4,6,0,1]

s = Solution2()
print(s.longestConsecutive(nums))