# Notes on solutions <!-- omit in toc -->

- [1. Two Sum](#1-two-sum)
- [2. Add Two Numbers](#2-add-two-numbers)
- [3. Longest Substring Without Repeating Characters](#3-longest-substring-without-repeating-characters)
- [4. Median of Two Sorted Arrays](#4-median-of-two-sorted-arrays)
- [167. Two Sum II - Input Array Is Sorted](#167-two-sum-ii---input-array-is-sorted)




<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>


## [1. Two Sum](https://leetcode.com/problems/two-sum/)

**Hash table approach**

- Time complexity: O(n)
- Space complexity: O(n)


```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cache_dict = {}

        for i in range(len(nums)):
            res = target - nums[i]
            if res in cache_dict:
                return [cache_dict[res], i]
            else:
                cache_dict[nums[i]] = i
```



<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>


## [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        root = node

        if not l1:
            return l2
        if not l2:
            return l1
        
        node.val += l1.val + l2.val
        carry = node.val // 10
        node.val = node.val % 10
        l1 = l1.next
        l2 = l2.next

        while l1 or l2 or carry > 0:
            node.next = ListNode(carry)
            node = node.next

            if l1:
                node.val += l1.val
                l1 = l1.next

            if l2:
                node.val += l2.val
                l2 = l2.next

            carry = node.val // 10
            node.val = node.val % 10

        return root
```


<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>


## [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Use one single pointer iterate through every char of the string, and with variable `start` recording the current substring without repeat char. Keep every char and its position in hash table for fast search (O(1)).

Whenever encountering a repeat char, all we need is to update the start of the target substring to be the next position of the repeat char (previous one). Anyway if this position is less than `start`, we won't update start (won't go back). 

That is to say, only the repeat char in the range of target substring is what we care about, which will be the pivot point for updating `start`. Those repeat chars in the position before current `start` are irrelevant. 

The length of current substring is `j - start + 1`. So in every iteration, just update max length to be the greater one of `maxlen, j - start + 1`.

- Time complexity: O(n)
- Space complexity: O(n)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_table = dict()
        maxlen = 0
        start = 0   # record the start pos of substring
        for j, c in enumerate(s):
            if c in char_table:
                start = max(start, char_table[c] + 1)  # update start pos if elligible
        
            maxlen = max(maxlen, j - start + 1) # update max length so far
            char_table[c] = j

        return maxlen
```


<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>

## [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

To get a median of a list of numbers, we have to sorted it first and get the exact element of the list if the length is an odd integer or the average of the middle two elements if the length is even. We can get the median with one statement: 

```python
median = (nums[int((len(nums) - 1) / 2)] + nums[int((len(nums) - 1) / 2 + .5)]) / 2
```

**Method 1**:

With two given sorted arrays, to get a median, we can just merge the two sorted arrays and compute the median.

To merge two sorted arrays the most direct way is to iterate the two arrays at the same time, who comes first stands out of the array and move to next and compare again. Until one array is exhausted, just concat the rest of the other. This operation is linear time. (m, n: size of two arrays).

- Time complexity: O(m+n)
- Space complexity: O(m+n)

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = self.mergeList(nums1, nums2)

        m = (len(nums) - 1) / 2
        return (nums[int(m)] + nums[int(m + .5)]) / 2

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

**Method 2**:

We can optimize the merging step by shrinking merging elements.

Compute medians of each array, say, `median1` and `median2`. If `median1` and `median2` are equal, we can tell this median is the median of two arrays. If `median1 < median2`, then the median of the two will be some number in the range from `median1` to `median2`. So, for each array, those numbers outside this range will be let alone, we don't need to bother to merge them. With this in mind, we can shrink the two sorted arrays significantly to much less elements. For example, 

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

**Binary search**. For `nums1`, we already know where `5` is and what we need to do is to find the *floor* element of `median2` in `nums1`. Vice versa, get the *ceiling* elemnt of `median1` in `nums2`. This operation might have time complexity of O(log(mn)). 

Furtherly, we actually don't need to concat left part arrays, only their length matters. So calculation of this problem (A) simply reduce to find the particular element in the middle part of arrays:

```python
m = (len - 1) / 2
median = (nums_middle[int(m - len_left)] + nums_middle[int(m + .5 - len_left)]) / 2
```

[full code](../solutions/4.%20Median%20of%20Two%20Sorted%20Arrays/median_two_sorted_3.py), this version runs for **113 ms**.

**Method 3**:

The analysis above can help think further, this problem can be transformed to another problem (B): 
***Find the i<sup>th</sup> element in two sorted arrays***

If we can find the i<sup>th</sup> element, all we need to do is to find the element(s) at `(m + n - 1) // 2` and `(m + n) / 2` to get the median. And also, we can compare medians to get two much smaller sorted arrays to reduce recursive cost.

To find the i<sup>th</sup> element in two sorted arrays, the method is analogue to find the middle part subarray in the range from `median1` to `median2` stated in the *Method2*. 
1. find the ceiling (smallest one greater than) of the start element of `nums2` in `nums1`, index is `k`. (use binary search)
2. if `i < k`, then return `nums1[i]`,
3. otherwise, cut `nums1` to `nums1[k:]`, exchange `nums1` and `nums2`, set `i` to `i-k`, repeat step 1.

Write it in recursive function, [full code](../solutions/4.%20Median%20of%20Two%20Sorted%20Arrays/median_two_sorted_4.py), the code runs for **156 ms**.

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

Since slicing operation in python is O(k) of [time complexity](https://wiki.python.org/moin/TimeComplexity), we can rewrite it without slicing, [full code](../solutions/4.%20Median%20of%20Two%20Sorted%20Arrays/median_two_sorted_7.py):

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

As a comparison, this version runs for **115 ms**. And recursion is more expensive than iteration in Python because it requires the allocation of a new stack frame every time. So we can further rewrite it in loops, [full code](../solutions/4.%20Median%20of%20Two%20Sorted%20Arrays/median_two_sorted_8.py):

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

## [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

**Hash table approach**

We can also solve this problem using hash table approach (see [1. Two Sum](#1-two-sum)). 

- Time complexity: O(n)
- Space complexity: O(n)


**Binary search approach**

Since the input array is sorted, we can easily think of the binary search method, which costs less space.

- Time complexity: O(nlogn)
- Space complexity: O(1)

```python
# binary search approach
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            lo = i + 1
            hi = len(numbers) - 1
            key = target - numbers[i]

            while lo <= hi:
                mid = math.floor((lo + hi) / 2)
                if key < numbers[mid]:
                    hi = mid - 1
                elif key > numbers[mid]:
                    lo = mid + 1
                else:
                    return [i+1, mid+1]
```

<details>

<summary>Ideas to improve the performance: </summary>


> In the binary search approach, we iterate from left to right with `i` and search for `target-numbers[i]` within all numbers to the right of number `i` by binary search. 
> 
> For `i`, at the end of `while` loop, if we don't get the match, `hi` will stop at some place, say, `j`. 
> 
> In the next iteration `i+1`, whether we get the match or not, after the `while` loop exits, `hi` will not be greater than `j`, since the input array is in non-decreasing order.
> 
> For example, `numbers = [1, 3, 4, 5, 8, 10, 13, 20, 21]`, `target = 15`. 
> 
> For `i = 0` (nubmer **1**), after `while` exit, `lo = 7`, `hi = 6`, `mid = 7`, we get `lo > hi`, which means we didn't get the sum match. 
> 
> Now, `hi` stops at number **13**. Increment `i` to move to the next number **3**, we actually don't need to bother considering the numbers on the right side of number 13 since the array is non-decreasing. 
> 
> Can we improve the performance of this binary search approach by using previous `hi` value in the next loop to reduce cost? In other words, in every iteration, we just update `lo` to start over from `i+1` and don't reset `hi` to `len(numbers) - 1`. With minor modification, the code looks like this:
> 
> ```python
> # binary search approach modification
> def twoSum(self, numbers: List[int], target: int) -> List[int]:
>     hi = len(numbers) - 1
>     for i in range(len(numbers)):
>         lo = i + 1
>         key = target - numbers[i]
> 
>         while lo <= hi:
>             mid = math.floor((lo + hi) / 2)
>             if key < numbers[mid]:
>                 hi = mid - 1
>             elif key > numbers[mid]:
>                 lo = mid + 1
>             else:
>                 return [i+1, mid+1]
> ```
> 
> This code solves the problem just like the original one, but the improvement is negligible for the binary search strategy. With the following example, we have so many duplicate numbers, so we will do a lot of binary search in vain.
> 
> `numbers = [1, 1, 1, 1, 1, 1, 1, 3, 4, 5, 8, 10, 13, 20], target = 15`
> 
> As `i` iterating through number **1**s, and the while loop doing the futile binary search, `hi` is just waiting at the position of number **13**. 
> 
> So, the usage of the binary search for this problem can be demoted to some pointer, which I call it lazy pointer `j`, starting from the rightmost, recording the possible position for `target-numbers[i]`. With this idea, we get the two-pointer approach.

</details>

**Two-pointer approach**

Use two pointers `i` and `j`, from left to right and from right to left, to find if `numbers[i] + numbers[j] == target` is successful. If less, move `i` a little to right, if greater, move `j` a little to left. This two-pointer approach is faster than binary search approach.

- Time complexity: O(n)
- Space complexity: O(1)

```python
# two-pointer approach
class Solution:
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
```





<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>

