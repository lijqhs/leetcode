
# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

To get a median of a sorted array `nums`: 

```python
median = (nums[(len(nums) - 1) // 2] + nums[len(nums) // 2]) / 2
```

**Method 1**:

<details>

<summary>With two given sorted arrays, to get a median, we can just merge the two sorted arrays and compute the median.</summary>
<br/>
To merge two sorted arrays the most direct way is to iterate the two arrays at the same time, who comes first stands out of the array and move to next and compare again. Until one array is exhausted, just concat the rest of the other. This operation is linear time.

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = self.mergeList(nums1, nums2)
        return (nums[(len(nums) - 1) // 2] + nums[len(nums) // 2]) / 2

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
```

</details>

**Method 2**:

<details>

<summary>We can optimize the merging step by shrinking merging elements.</summary>
<br/>

Compute medians of each array, say, `median1` and `median2`. If `median1` and `median2` are equal, we can tell this median is the median of two arrays. If `median1 < median2`, then the median of the two arrays will be some number in the range from `median1` to `median2`. So, for each array, those numbers outside this range will be let alone, we don't need to bother to merge them. With this in mind, we can shrink the two sorted arrays significantly to much less elements. For example, 

```python
nums1 = [1,3,5,11,12]   # median1 = 5
nums2 = [2,4,7,8,9,13]  # median2 = 7.5
```
For `nums1`, we don't care `1,3` (left side elements) and `11,12` (right side elements), and for `nums2`, `2,4` (left side elements) and `9,13` (right side elements). We won't iterate these elements in the merging step. Instead of merging `nums1` and `nums2`, we just merge `[5]` (middle part elements) and `[7,8]` (middle part elements), which is `[5,7,8]` by much less iteration. To get a whole array, just extend the list by (left, middle, right): `[1,3] + [2,4] + [5,7,8] + [11,12] + [9,13]` (for those in the left or right side, order doesn't matter):

```python
nums = [1,3,2,4,5,7,8,11,12,9,13]   # median = 7
```
We don't need to get a sorted version to get a median! Unfortunately, [time complexity](https://wiki.python.org/moin/TimeComplexity) of list extend operation in python is O(n).

*Now, how to get the middle side elements of each array effieciently?*

**Binary search**. For `nums1`, we already know where `5` is and what we need to do is to find the *floor* element of `median2` in `nums1`. Vice versa, get the *ceiling* elemnt of `median1` in `nums2`. Use binary search to do this, which might totally have time complexity of O(log(mn)) in this case. 

Furthermore, we actually don't need to concat left part arrays, only their length matters. So calculation of this problem (A) simply reduces to find the particular element in the middle part of arrays:

```python
median = (nums_middle[(len - 1) // 2 - len_left] + nums_middle[len // 2 - len_left]) / 2
```

[full code](median_two_sorted_3.py), this version runs for **113 ms**.

</details>

**Method 3**:

<details>

<summary>The analysis above can help think further, this problem can be transformed to another problem (B): 

***Find the i<sup>th</sup> element in two sorted arrays***
</summary>

If we can find the i<sup>th</sup> element, all we need to do is to find the element(s) at `(m + n - 1) // 2` and `(m + n) / 2` to get the median. And also, we can compare medians to get two much smaller sorted arrays to reduce recursive cost.

To find the i<sup>th</sup> element in two sorted arrays, the method is analogue to find the middle part subarray in the range from `median1` to `median2` stated in the *Method2*. Use the binary search to find the left side element of each array which gradually approaches the target.

1. find the ceiling (smallest one greater than) of the start element of `nums2` in `nums1`, index is `k`. (use binary search)
2. if `i < k`, then return `nums1[i]`,
3. otherwise, cut `nums1` to `nums1[k:]`, exchange `nums1` and `nums2`, set `i` to `i-k`, repeat step 1.

Write it in recursive function, [full code](median_two_sorted_4.py), the code runs for **156 ms**.

```python
def findElement(self, nums1, nums2, index):
    """
    find the element at index of the two sorted arrays, recursively
    return: a list containing the element
    """

    if (len(nums1) == 0): return nums2[index:index+1]   # can be [] if index out of range
    if (len(nums2) == 0): return nums1[index:index+1]   # can be [] if index out of range

    cut1 = self.getCeilingNoEqual(nums1, nums2[0])
    if (cut1 > index): return nums1[index:index+1]
    else: 
        return self.findElement(nums2, nums1[cut1:], index - cut1)
```

Since slicing operation in python is O(k) of [time complexity](https://wiki.python.org/moin/TimeComplexity), we can rewrite it without slicing, [full code](median_two_sorted_7.py):

```python
def findElement2(self, nums1, left1, right1, nums2, left2, right2, index):
    """
    find the element at index of the two sorted arrays, recursively
    index: full scope index (absolute position)
    return: the element
    """

    if (left1 >= right1): return index - left1 < right2 and nums2[index - left1] or None 
    if (left2 >= right2): return index - left2 < right1 and nums1[index - left2] or None 

    newLeft1 = self.getCeilingNoEqual(nums1, left1, right1, nums2[left2])
    if (newLeft1 > index - left2): 
        return nums1[index - left2]
    else: 
        return self.findElement2(nums2, left2, right2, nums1, newLeft1, right1, index)
```

As a comparison, this version runs for **115 ms**. And recursion is more expensive than iteration in Python because it requires the allocation of a new stack frame every time. So we can further rewrite it in loops, [full code](median_two_sorted_8.py):

```python
def findElement3(self, nums1, left1, right1, nums2, left2, right2, index):
    while True:
        if (left1 >= right1): return index - left1 < right2 and nums2[index - left1] or None 
        if (left2 >= right2): return index - left2 < right1 and nums1[index - left2] or None 

        newLeft1 = self.getCeilingNoEqual(nums1, left1, right1, nums2[left2])
        if (newLeft1 > index - left2): 
            return nums1[index - left2]
        else: 
            nums1, nums2 = nums2, nums1
            left1, left2 = left2, newLeft1
            right1, right2 = right2, right1
```

It runs for **101 ms**.

But `findElement` to find i<sup>th</sup> element is not optimal, every step needs a binary search. The core idea in this method is to use a left hand to approch the target i<sup>th</sup> element. If the target is at the right side, it needs more time. For example, if we want to find `17`th element, this function costs nearly `nlogn`. To find the right side target, it is better to use right hand to approach the target (should call some `getFloorNoEqual` in the iteration). So although this function can solve the problem, it is not *balanced* and the time complexity is approximately O(min(mlogn, nlogm)). Right side target costs more time than left side target due to its intrinsic unbalanced logic.

```python
nums1 = [1,2,3,4,5,6,7,8,9]
nums2 = [1,2,3,4,5,6,7,8,9]
```

Recall that at the beginning of *Method2* we state that if `median1 < median2` then the median of the two arrays will be some number in the range from `median1` to `median2`. This is equivalent to that the target median will be not in the left half of `nums1` or the right half of `nums2`. If `i` (i<sup>th</sup> element) is greater than the index of the target median, then it is certain that i<sup>th</sup> element will be in the left half of `nums1`. Vice versa, if `i` is less than the median index, i<sup>th</sup> element will be in the right half of `nums2`.

Generally for k1<sup>th</sup> in `nums1` and k2<sup>th</sup> in `nums2`, if `i > k1 + k2`, and `nums1[k1] < nums2[k2]`. Then i<sup>th</sup> will be certainly not in the subarray in the left of k1<sup>th</sup>. So we can also use binary search idea to approach the target i<sup>th</sup> by using median index in every iteration. 

```python
def findElement4(self, nums1, left1, right1, nums2, left2, right2, index):
    while True:
        if (left1 > right1): return nums2[index - left1]
        if (left2 > right2): return nums1[index - left2]

        i1 = (left1 + right1) // 2
        i2 = (left2 + right2) // 2

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
```

It runs for **93 ms**. [full code](median_two_sorted_9.py). Time complexity is O(log(m)+log(n)) < O(log(m+n)).

</details>


<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>

