## [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

This problem can be accomplished via intuitively by using two pointers, from leftmost and from rightmost, which can form the most widest container. Within each step, skip a shorter vertical line. The time complexity is O(n).

```python
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
```

The code can be simplified to only a few lines since only `maxArea` is what we want:

```python
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
```


<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>
