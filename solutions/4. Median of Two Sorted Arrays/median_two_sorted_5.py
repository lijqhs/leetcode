
import re
from typing import List


class Solution5:

    """ 
    optimized version of Solution4. (compare medians to shrink arrays)
    
    don't need concat left part list and right part 
    only need length of left part list len_left
    so the index of median in the middle part list is calculated by:

    m = (len - 1) / 2
    median = (nums_middle[int(m - len_left)] + nums_middle[int(m + .5 - len_left)]) / 2

    So this problem (A) can be transformed to another problem (B): 
    *** Find the ith element in two sorted arrays ***

    If this problem solved, we do not need to get the floor of median2 (bigger one).
    That is to say, we only need to care the smaller median, and with this lower bound 
    to slice two arrays as left part (only its length matters) and middle_right part. 
    
    And then find the element [int(m - len_left), int(m + .5 - len_left)] in the middle_right part.

    Wait... If we have already solved the problem B, why do we bother to compare two medians???

    All we need to do is to find the element(s) at int((m + n - 1) / 2) and int((m + n) / 2).

    Anyway, we can compare medians to get two much smaller sorted arrays to reduce recursive cost.

    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        median1 = self.median(nums1)
        median2 = self.median(nums2)

        if (median1 == None): return median2
        if (median2 == None): return median1

        if (median1 == median2): return median1

        if (median1 < median2):
            return self.getMedian(nums1, nums2)
        else:
            return self.getMedian(nums2, nums1)


    def getMedian(self, nums1, nums2):
        # median1 < median2

        m1 = int((len(nums1) - 1) / 2)
        m2 = int(len(nums2) / 2)    # len2 is odd, the middle one; len2 is even, the middle right one

        median1 = self.median(nums1)
        median2 = self.median(nums2)

        right = self.getFloor(nums1[m1:], median2) + m1
        left = self.getCeiling(nums2[:m2+1], median1)

        m = (len(nums1) + len(nums2) - 1) / 2

        len_left = m1 + left
        med1 = int(m - len_left)
        med2 = int(m + .5 - len_left)


        if (med1 == med2):
            x = self.findElement(nums1[m1:right+1], nums2[left:m2+1], med1)
            if x:
                return x[0]
        else:
            x1 = self.findElement(nums1[m1:right+1], nums2[left:m2+1], med1)
            x2 = self.findElement(nums1[m1:right+1], nums2[left:m2+1], med2)
            if x1 and x2:
                return (x1[0] + x2[0]) / 2


    def findElement(self, nums1, nums2, index):
        """
        find the element at index of the two sorted arrays, recursively
        """

        if (len(nums1) == 0): return nums2[index:index+1]   # can be [] if index out of range
        if (len(nums2) == 0): return nums1[index:index+1]   # can be [] if index out of range

        cut1 = self.getCeilingNoEqual(nums1, nums2[0])
        if (cut1 > index): return nums1[index:index+1]
        else: 
            return self.findElement(nums2, nums1[cut1:], index - cut1)


    def getCeilingNoEqual(self, nums, bound):
        # get index of smallest element greater than bound
        if (nums[-1] <= bound): return len(nums)

        l, r = 0, len(nums) - 1
        mid = int((l + r) / 2)

        while (l < r):
            if (nums[mid] > bound):
                r = mid
                mid = int((l + r) / 2)
            else:
                l = mid + 1
                mid = int((l + r) / 2)

        return mid


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


    def median(self, nums):
        if (not nums): return None

        m = (len(nums) - 1) / 2
        return (nums[int(m)] + nums[int(m + .5)]) / 2


if __name__ == "__main__":
    nums1 = [3,5,6]
    nums2 = [3,8,9,13,14]

    # nums1 = [0,0]
    # nums2 = [0,0]

    s = Solution5()

    # print("ceiling: ", s.getCeiling(nums1, 13))
    # print(s.findElement(nums1, nums2, 1))
    # print(s.getCeilingNoEqual(nums1, 0))

    # print("nums1:", nums1)
    # print("nums2:", nums2)

    # print("median1:", s.median(nums1))
    # print("median2:", s.median(nums2))
    print("median:", s.findMedianSortedArrays(nums1, nums2))