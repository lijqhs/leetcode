import time

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cache_dict = {}

        for i in range(len(nums)):
            res = target - nums[i]
            if res in cache_dict:
                return [cache_dict[res], i]
            else:
                cache_dict[nums[i]] = i
            
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