
import re
from typing import List

class Solution:
    """
    method1: merge two sorted arrays
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = self.mergeList(nums1, nums2)

        m = (len(nums) - 1) / 2
        return (nums[int(m)] + nums[int(m + .5)]) / 2

    def mergeList(self, nums1, nums2):
        nums = []

        if (len(nums1) == 0): return nums2
        if (len(nums2) == 0): return nums1

        i, j = 0, 0
        while (i < len(nums1) or j < len(nums2)):
            if (i == len(nums1)):
                nums.extend(nums2[j:])
                break

            if (j == len(nums2)):
                nums.extend(nums1[i:])
                break

            if (nums1[i] < nums2[j]):
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        return nums


if __name__ == "__main__":
    nums1 = [0,1,3,5,6,7,12]
    nums2 = [2,4,7,8,9,13]

    s = Solution()

    print("nums1:", nums1)
    print("nums2:", nums2)

    print("median:", s.findMedianSortedArrays(nums1, nums2))