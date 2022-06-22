
import re
from typing import List


class Solution2:
    """
    method2: get middle part of two arrays by comparing two medians to shrink arrays to merge

    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        median1 = self.median(nums1)
        median2 = self.median(nums2)

        if (median1 == None): return median2
        if (median2 == None): return median1

        if (median1 == median2): return median1

        if (median1 < median2):
            nums = self.mergeConcat(nums1, nums2)
        else:
            nums = self.mergeConcat(nums2, nums1)

        # print(nums)
        
        return self.median(nums)


    def mergeConcat(self, nums1, nums2):
        # median1 < median2

        m1 = int((len(nums1) - 1) / 2)
        m2 = int(len(nums2) / 2)    # len2 is odd, the middle one; len2 is even, the middle right one

        median1 = self.median(nums1)
        median2 = self.median(nums2)

        right = self.getFloor(nums1[m1:], median2) + m1
        left = self.getCeiling(nums2[:m2+1], median1)

        nums_middle = self.mergeList(nums1[m1:right+1], nums2[left:m2+1])
        nums = nums1[:m1]+nums2[:left]+nums_middle+nums1[right+1:]+nums2[m2+1:]
        
        return nums


    def getFloor(self, nums, bound):
        # get index of largest element less than or equal bound
        if (nums[0] > bound): return -1

        l, r = 0, len(nums) - 1
        mid = int((l + r) / 2)

        while (l <= r):
            if (nums[mid] > bound):
                r = mid - 1
                mid = int((l + r) / 2)
            else:
                l = mid + 1
                mid = int((l + r) / 2)

        return mid


    def getCeiling(self, nums, bound):
        # get index of smallest element greater than or equal bound
        if (nums[-1] < bound): return len(nums)

        l, r = 0, len(nums) - 1
        mid = int((l + r) / 2)

        while (l < r):
            if (nums[mid] >= bound):
                r = mid
                mid = int((l + r) / 2)
            else:
                l = mid + 1
                mid = int((l + r) / 2)

        return mid

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


    def median(self, nums):
        if (not nums): return None

        m = (len(nums) - 1) / 2
        return (nums[int(m)] + nums[int(m + .5)]) / 2



if __name__ == "__main__":
    nums1 = [0,1,3,5,6,7,12]
    nums2 = [2,4,7,8,9,13]

    s = Solution2()
    # m = s.findMedianSortedArrays(nums1, nums2)

    # print("median: ")
    # print(m)

    # nums = [1, 3, 4, 7, 8, 8, 8, 8, 10, 19]

    # mid = s.getFloor(nums, 2)


    print("nums1:", nums1)
    print("nums2:", nums2)

    print("median1:", s.median(nums1))
    print("median2:", s.median(nums2))
    print("median:", s.findMedianSortedArrays(nums1, nums2))