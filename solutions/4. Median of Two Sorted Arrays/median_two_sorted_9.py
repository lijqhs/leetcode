
import re
from typing import List


class Solution9:

    """ 
    use binary search to approach target ith element
    nonrecursive version
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        index1 = (len(nums1) + len(nums2) - 1) // 2
        index2 = (len(nums1) + len(nums2)) // 2

        if (index1 == index2):
            return self.findElement4(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, index1)
        else:
            x1 = self.findElement4(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, index1)
            x2 = self.findElement4(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, index2)
            return (x1 + x2) / 2


    def findElement4(self, nums1, left1, right1, nums2, left2, right2, index):
        while True:

            if (left1 > right1): return nums2[index - left1]
            if (left2 > right2): return nums1[index - left2]

            i1 = (left1 + right1) // 2
            i2 = (left2 + right2) // 2

            print(index)

            num1, num2 = nums1[i1], nums2[i2]

            if index <= i1 + i2:
                if num1 < num2:
                    right2 = i2 - 1
                else:
                    right1 = i1 - 1
            else:
                if num1 < num2:
                    left1 = i1 + 1
                else:
                    left2 = i2 + 1


    # for debug use
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
    nums1 = [3,5,6]
    nums2 = [3,8,9,13,14]

    # nums1 = [1,2,3,4,5,6,7,8,9]
    # nums2 = [1,2,3,4,5,6,7,8,9]

    # nums1 = [1,1,1,1,1,1,1,1,1]
    # nums2 = [1,1,1,1,1,1,1,1,1]

    # nums1 = [1,2]
    # nums2 = [3,4]

    # nums1 = [0,0]
    # nums2 = [0,0]

    s = Solution9()

    # print("median:", s.findMedianSortedArrays(nums1, nums2))
    # print(s.findElement4(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, 2))
    m = (len(nums1) + len(nums2)) // 2
    print(s.findElement5(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, m))
    print(s.mergeList(nums1, nums2))
