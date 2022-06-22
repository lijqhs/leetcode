
import re
from typing import List


class Solution6:

    """ 
    optimized version of Solution5. 
    - (compare medians to shrink arrays)
    - (avoid usage of slicing in python, time complexity is O(k))
    
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

    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

    #     median1 = self.median(nums1)
    #     median2 = self.median(nums2)

    #     if (median1 == None): return median2
    #     if (median2 == None): return median1

    #     if (median1 == median2): return median1

    #     if (median1 < median2):
    #         return self.getMedian(nums1, nums2)
    #     else:
    #         return self.getMedian(nums2, nums1)


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        median1 = self.median(nums1)
        median2 = self.median(nums2)

        if (median1 == None): return median2
        if (median2 == None): return median1

        if (median1 == median2): return median1

        return self.getMedianAll(nums1, nums2)


    def getMedianAll(self, nums1, nums2):
        # median1 < median2

        index1 = (len(nums1) + len(nums2) - 1) // 2
        index2 = (len(nums1) + len(nums2)) // 2

        if (index1 == index2):
            return self.findElement2(nums1, 0, len(nums1), nums2, 0, len(nums2), index1)
        else:
            x1 = self.findElement2(nums1, 0, len(nums1), nums2, 0, len(nums2), index1)
            x2 = self.findElement2(nums1, 0, len(nums1), nums2, 0, len(nums2), index2)
            if x1 and x2:
                return (x1 + x2) / 2


    def getMedian(self, nums1, nums2):
        # median1 < median2

        left1 = int((len(nums1) - 1) / 2)
        right2 = int(len(nums2) / 2)    # len2 is odd, the middle one; len2 is even, the middle right one

        median1 = self.median(nums1)
        median2 = self.median(nums2)

        right1 = self.getFloor(nums1, left1, len(nums1), median2) + left1
        left2 = self.getCeiling(nums2, 0, right2+1, median1)

        med1 = (len(nums1) + len(nums2) - 1) // 2
        med2 = (len(nums1) + len(nums2)) // 2


        if (med1 == med2):
            return self.findElement(nums1, left1, right1+1, nums2, left2, right2+1, med1 - left1 - left2)
        else:
            x1 = self.findElement(nums1, left1, right1+1, nums2, left2, right2+1, med1 - left1 - left2)
            x2 = self.findElement(nums1, left1, right1+1, nums2, left2, right2+1, med2 - left1 - left2)
            if x1 and x2:
                return (x1 + x2) / 2


    def findElement2(self, nums1, left1, right1, nums2, left2, right2, index):
        """
        find the element at index of the two sorted arrays, recursively

        index: full scope index (absolute position)
        """

        if (left1 >= right1): return index - left1 < right2 and nums2[index - left1] or None 
        if (left2 >= right2): return index - left2 < right1 and nums1[index - left2] or None 

        newLeft1 = self.getCeilingNoEqual(nums1, left1, right1, nums2[left2])
        print("left1, left2, newLeft1, index: ", left1, left2, newLeft1, index)
        if (newLeft1 > index - left2): 
            return nums1[index - left2]
        else: 
            return self.findElement2(nums2, left2, right2, nums1, newLeft1, right1, index)


    def findElement(self, nums1, left1, right1, nums2, left2, right2, index):
        """
        find the element at index of the two sorted arrays, recursively

        index: relative position

        """

        if (left1 >= right1): return index + left2 < right2 and nums2[index + left2] or None 
        if (left2 >= right2): return index + left1 < right1 and nums1[index + left1] or None 

        cut1 = self.getCeilingNoEqual(nums1, left1, right1, nums2[left2])
        if (cut1 > index + left1): 
            return nums1[index + left1]
        else: 
            return self.findElement(nums2, left2, right2, nums1, cut1, right1, index + left1 - cut1)


    def getCeilingNoEqual(self, nums, left, right, bound):
        # get index of smallest element greater than bound
        if (nums[right-1] <= bound): return right

        l, r = left, right - 1
        mid = (l + r) // 2

        while (l < r):
            if (nums[mid] > bound):
                r = mid
                mid = (l + r) // 2
            else:
                l = mid + 1
                mid = (l + r) // 2

        return mid


    def getFloor(self, nums, left, right, bound):
        # get index of largest element less than or equal bound
        if (nums[left] > bound): return -1

        l, r = left, right - left - 1
        mid = (l + r) // 2

        while (l <= r):
            if (nums[mid] > bound):
                r = mid - 1
                mid = (l + r) // 2
            else:
                l = mid + 1
                mid = (l + r) // 2

        return mid


    def getCeiling(self, nums, left, right, bound):
        # get index of smallest element greater than or equal bound
        if (nums[right - 1] < bound): return right

        l, r = left, right - 1
        mid = (l + r) // 2

        while (l < r):
            if (nums[mid] >= bound):
                r = mid
                mid = (l + r) // 2
            else:
                l = mid + 1
                mid = (l + r) // 2

        return mid


    def median(self, nums):
        if (not nums): return None

        m = (len(nums) - 1) / 2
        return (nums[int(m)] + nums[int(m + .5)]) / 2


if __name__ == "__main__":
    nums1 = [3,5,6]
    nums2 = [3,8,9,13,14]

    # nums1 = [1,2]
    # nums2 = [3,4]

    s = Solution6()

    # print("ceiling: ", s.getCeilingNoEqual(nums2, 1, 3, 14))
    # print(s.findElement(nums1, nums2, 1))
    # print(s.getCeilingNoEqual(nums1, 0))

    # print("nums1:", nums1)
    # print("nums2:", nums2)

    # print("median1:", s.median(nums1))
    # print("median2:", s.median(nums2))
    print("median:", s.findMedianSortedArrays(nums1, nums2))
    # print("find: ", s.findElement2(nums1, 0, 3, nums2, 0, 5, 1))
