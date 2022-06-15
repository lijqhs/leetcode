
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()

        print("input: ", end='')

        for i in range(len(nums)):
            nums_index = nums_dict.get(nums[i], [])
            nums_index.append(i)
            nums_dict.update({nums[i]: nums_index})
            print(nums[i], end=' ')


        print("target: ", end='')
        print(target)

        print("dict: " + str(nums_dict))

        for i in range(len(nums)):
            res = target - nums[i]
            res_ind = nums_dict.get(target - nums[i], [])
            if res_ind:
                if nums[i] == res:
                    if len(res_ind) < 2:
                        continue
                    else:
                        return res_ind[:2]
                else:
                    return [i] + res_ind[:1]
            
        return []





if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
    print()
    print(s.twoSum([3,2,4], 6))
    print()
    print(s.twoSum([3, 3], 6))