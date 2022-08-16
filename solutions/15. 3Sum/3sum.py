from typing import List

class Solution:
    """
    Bad: Time Limit Exceeded
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        k = len(nums)-1

        while k > 1:
            i = 0
            while i < k:
                j = i + 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        t = tuple(sorted([nums[i], nums[j], nums[k]]))
                        res.add(t)
                    j += 1
                i += 1
            k -= 1

        return res


class Solution1:
    """
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        i = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j, k = i + 1, len(nums)-1

            while j < k:
                x = nums[i] + nums[j] + nums[k]
                if x > 0:
                    k -= 1
                elif x < 0:
                    j += 1
                else: # x == 0
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k: j += 1

        return res


nums = [-1,0,1,2,-1,-4]

s = Solution1()
print(s.threeSum(nums))
            
