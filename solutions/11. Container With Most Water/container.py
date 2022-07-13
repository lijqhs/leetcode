
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = i = 0
        right = j = len(height) - 1

        minHeight = min(height[left], height[right])
        maxArea = minHeight * (right - left)

        while i < j:

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

            mH = min(height[i], height[j])
            if mH < minHeight:
                continue

            area = mH * (j - i)
            if area > maxArea:
                left = i
                right = j
                minHeight = mH
                maxArea = area
                # print("left: ", left, height[left])
                # print("right: ", right, height[right])

        return maxArea
        # return left, right, maxArea


class Solution2:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        maxArea = 0

        while i < j:

            area = min(height[i], height[j]) * (j - i)
            if area > maxArea:
                maxArea = area

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxArea



if __name__ == "__main__":

    # height = [1,8,6,2,5,4,8,3,7]
    # height = [1, 1]
    height = [2,3,4,5,18,17,6]

    s = Solution2()
    print(s.maxArea(height))
                

