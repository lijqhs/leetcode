
import re
from typing import List


class Solution4:

    """ 
    optimized version of Solution3.
    
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

        m = len(nums1)
        n = len(nums2)

        med1 = int((m + n - 1) / 2)
        med2 = int((m + n) / 2)

        if (med1 == med2):
            num = self.findElement(nums1, nums2, med1)
            if num:
                return num[0]
        else:
            num1 = self.findElement(nums1, nums2, med1)
            num2 = self.findElement(nums1, nums2, med2)
            if num1 and num2:
                return (num1[0] + num2[0]) / 2


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



if __name__ == "__main__":
    # nums1 = [3,5,6]
    # nums2 = [3,8,9,13,14]

    nums1 = [0,0]
    nums2 = [0,0]

    s = Solution23()

    # print("ceiling: ", s.getCeiling(nums1, 13))
    # print(s.findElement(nums1, nums2, 1))
    # print(s.getCeilingNoEqual(nums1, 0))

    # print("nums1:", nums1)
    # print("nums2:", nums2)

    # print("median1:", s.median(nums1))
    # print("median2:", s.median(nums2))
    print("median:", s.findMedianSortedArrays(nums1, nums2))