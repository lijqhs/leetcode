
import re
from typing import List


class Solution7:

    """ 
    clear version of Solution6
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        median1 = self.median(nums1)
        median2 = self.median(nums2)

        if (median1 == None): return median2
        if (median2 == None): return median1

        if (median1 == median2): return median1

        # way 1
        # return self.getMedianAll(nums1, nums2)  # this costs more time than way 2

        # way 2
        if (median1 < median2):
            return self.getMedian(nums1, nums2)
        else:
            return self.getMedian(nums2, nums1)


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

        index1 = (len(nums1) + len(nums2) - 1) // 2
        index2 = (len(nums1) + len(nums2)) // 2

        if (index1 == index2):
            return self.findElement2(nums1, left1, right1+1, nums2, left2, right2+1, index1)
        else:
            x1 = self.findElement2(nums1, left1, right1+1, nums2, left2, right2+1, index1)
            x2 = self.findElement2(nums1, left1, right1+1, nums2, left2, right2+1, index2)
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
        if (newLeft1 > index - left2): 
            return nums1[index - left2]
        else: 
            return self.findElement2(nums2, left2, right2, nums1, newLeft1, right1, index)


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
    # nums1 = [3,5,6]
    # nums2 = [3,8,9,13,14]

    # nums1 = [1,2]
    # nums2 = [3,4]

    nums1 = [0,0]
    nums2 = [0,0]

    s = Solution7()

    # print("ceiling: ", s.getCeilingNoEqual(nums2, 1, 3, 14))
    # print(s.findElement(nums1, nums2, 1))
    # print(s.getCeilingNoEqual(nums1, 0))

    # print("nums1:", nums1)
    # print("nums2:", nums2)

    # print("median1:", s.median(nums1))
    # print("median2:", s.median(nums2))
    print("median:", s.findMedianSortedArrays(nums1, nums2))
    # print("find: ", s.findElement2(nums1, 0, 3, nums2, 0, 5, 1))
