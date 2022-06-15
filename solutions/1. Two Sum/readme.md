# 1. Two Sum

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

**Example 3:**

    Input: nums = [3,3], target = 6
    Output: [0,1]

**Constraints:**

- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- Only one valid answer exists.

**Follow-up:** Can you come up with an algorithm that is less than O(n2) time complexity?


### Solution 1:

**Brute force** in Java:


```java
class Solution {
    public static int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    result[0] = i;
                    result[1] = j;
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;

        int[] result = twoSum(nums, target);
        for (int i = 0; i < result.length; i++)
            System.out.print(result[i] + " ");
        System.out.println();
    }
}
```


### Solution 2

**Hash table solution**

Python in O(n) time.

```python
import time
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache_dict = {}

        for i in range(len(nums)):
            res = target - nums[i]
            if res in cache_dict:
                return [cache_dict[res], i]
            else:
                cache_dict[nums[i]] = i
            


if __name__ == '__main__':
    s = Solution()
    start = time.time()
    print(s.twoSum([2,7,11,15], 9))
    print()
    print(s.twoSum([3,2,4], 6))
    print()
    print(s.twoSum([3, 3], 6))
    print()
    print("cost time: " + str(time.time() - start))
```