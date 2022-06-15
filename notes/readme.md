# Notes on solutions



## [1. Two Sum](https://leetcode.com/problems/two-sum/)

**Hash table approach**

- Time complexity: O(N)
- Space complexity: O(N)


```python
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




## [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

**Hash table approach**

We can also solve this problem using hash table approach (see [1. Two Sum](#1-two-sum)). 

- Time complexity: O(N)
- Space complexity: O(N)


**Binary search approach**

Since the input array is sorted, we can easily think of the binary search method, which costs less space.

- Time complexity: O(NlogN)
- Space complexity: O(1)

```python
# binary search approach
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

- Time complexity: O(N)
- Space complexity: O(1)

```python
# two-pointer approach
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

