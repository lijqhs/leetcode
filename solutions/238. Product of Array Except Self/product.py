from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # traverse 2 times
        # first, calculate prefix product
        prod = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            prod[i] = prefix
            prefix *= nums[i]

        # second, calculate suffix product
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            prod[i] *= suffix
            suffix *= nums[i]

        return prod

nums = [1,2,3,4]
s = Solution()
print(s.productExceptSelf(nums))