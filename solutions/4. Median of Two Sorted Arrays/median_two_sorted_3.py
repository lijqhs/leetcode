
import re
from typing import List


class Solution3:

    """ 
    optimized version of Solution2.

    don't need concat left part list and right part 
    only need length of left part list len_left
    so the index of median in the middle part list is calculated by:

    m = (len - 1) / 2
    median = (nums_middle[int(m - len_left)] + nums_middle[int(m + .5 - len_left)]) / 2
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        median1 = self.median(nums1)
        median2 = self.median(nums2)

        if (median1 == None): return median2
        if (median2 == None): return median1

        if (median1 == median2): return median1

        if (median1 < median2):
            len_left, nums_middle = self.mergeConcat(nums1, nums2)
        else:
            len_left, nums_middle = self.mergeConcat(nums2, nums1)

        # print(nums_middle)
        
        return self.medianMerged(nums_middle, len_left, len(nums1) + len(nums2))


    def mergeConcat(self, nums1, nums2):
        # median1 < median2

        m1 = int((len(nums1) - 1) / 2)
        m2 = int(len(nums2) / 2)    # len2 is odd, the middle one; len2 is even, the middle right one

        median1 = self.median(nums1)
        median2 = self.median(nums2)

        right = self.getFloor(nums1[m1:], median2) + m1
        left = self.getCeiling(nums2[:m2+1], median1)

        nums_middle = self.mergeList(nums1[m1:right+1], nums2[left:m2+1])
        
        return m1 + left, nums_middle


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


    def medianMerged(self, nums_middle, len_left, len):
        if (not nums_middle): return None

        m = (len - 1) / 2
        return (nums_middle[int(m - len_left)] + nums_middle[int(m + .5 - len_left)]) / 2



if __name__ == "__main__":
    nums1 = [0,1,3,5,6,7,12]
    nums2 = [2,4,7,8,9,13]

    s = Solution3()

    print("nums1:", nums1)
    print("nums2:", nums2)

    print("median1:", s.median(nums1))
    print("median2:", s.median(nums2))
    print("median:", s.findMedianSortedArrays(nums1, nums2))