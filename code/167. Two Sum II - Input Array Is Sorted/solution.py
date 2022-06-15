import re
import time
from typing import List
import math


# base 
class Solution:
    """
    hash table solution
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache_dict = {}

        for i in range(len(numbers)):
            res = target - numbers[i]
            if res in cache_dict:
                return [cache_dict[res] + 1, i + 1]
            else:
                cache_dict[numbers[i]] = i
            
        return []


class Solution2:
    """
    binary search solution

    https://en.wikipedia.org/wiki/Binary_search_algorithm
    """ 

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            j = self.search(numbers, target - numbers[i])
            if (j >= 0):
                return [i+1, j+1]

        return []

    
    def search(self, nums: List[int], key: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo != hi:
            mid = math.ceil((lo + hi) / 2)
            if key < nums[mid]:
                hi = mid - 1
            else:
                lo = mid
        
        if nums[lo] == key:
            return lo
        
        return -1

        
class Solution3:
    """
    binary search solution

    put binary search in the loop
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            lo = i + 1
            hi = len(numbers) - 1
            key = target - numbers[i]

            while lo != hi:
                mid = math.ceil((lo + hi) / 2)
                if key < numbers[mid]:
                    hi = mid - 1
                else:
                    lo = mid
            
            if numbers[lo] == key:
                return [i+1, lo+1]

class Solution33:
    """
    binary search solution

    put binary search in the loop
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            lo = i + 1
            hi = len(numbers) - 1
            key = target - numbers[i]
            
            print()

            while lo <= hi:
                mid = math.floor((lo + hi) / 2)
                print("lo:", lo, " hi:", hi, " mid:", mid)
                if key < numbers[mid]:
                    hi = mid - 1
                    print("<<< hi:  ", hi)
                elif key > numbers[mid]:
                    lo = mid + 1
                    print(">>> lo:  ", lo)
                else:
                    return [i+1, mid+1]
            

class Solution333:
    """
    binary search solution

    put binary search in the loop
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hi = len(numbers) - 1
        for i in range(len(numbers)):
            lo = i + 1
            key = target - numbers[i]
            
            print()

            while lo <= hi:
                mid = math.floor((lo + hi) / 2)
                print("lo:", lo, " hi:", hi, " mid:", mid)
                if key < numbers[mid]:
                    hi = mid - 1
                    print("<<< hi:  ", hi)
                elif key > numbers[mid]:
                    lo = mid + 1
                    print(">>> lo:  ", lo)
                else:
                    return [i+1, mid+1]
            


class Solution4:
    """
    two-pointer solution
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1

        while lo < hi:
            if (numbers[lo] + numbers[hi] == target):
                return [lo + 1, hi + 1]
            if (numbers[lo] + numbers[hi] < target):
                lo += 1
            else:
                hi -= 1



if __name__ == '__main__':
    s = Solution333()
    start = time.time()
    # print(s.twoSum([2,7,11,15], 9))
    # print()
    # print(s.twoSum([2,3,4], 6))
    # print()
    # print(s.twoSum([3, 3, 3, 3, 3, 3, 3], 6))
    # print()
    # print(s.twoSum([1, 3, 4, 5, 8, 10, 13, 20, 21], 15))
    # print()
    # print(s.twoSum([0, 1, 3, 4, 5, 8, 10, 13, 20, 21], 15))
    # print()
    print(s.twoSum([1, 1, 1, 1, 1, 1, 1, 3, 4, 5, 8, 10, 13, 20], 15))
    print()
    print("cost time: " + str(time.time() - start))