import time

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        wait_dict = {}

        for i in range(len(nums)):
            res = target - nums[i]
            if res in wait_dict:
                return [wait_dict[res], i]
            else:
                wait_dict[nums[i]] = i
            
        return []





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