## [15. 3Sum](https://leetcode.com/problems/3sum/)

>Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
>
>Notice that the solution set must not contain duplicate triplets.


Main ideas:
- sort the list
- traverse the list from left to right
- for each element, go through the list after it from two ends of the list
- determine how to increment each step by the sign of the sum of the three numbers
- for inner iteration, skip same numbers if we get triplets
- for outer iteration, skip same numbers


```python
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
```