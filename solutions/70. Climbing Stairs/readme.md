## [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

If we count steps from top to bottom, things will be more easier to understand. 
- Start from the topmost stair which is the 0<sup>th</sup> level, we have the only one way to the top since we are already at the top. 
- Then the next down step is the 1<sup>st</sup> level, we have the only one way to the top since we can only climb 1 step to the top.
- Then at 2<sup>nd</sup> level, we have two options, climbing 1 step to the 1<sup>st</sup> level which has one way to the top and climbing 2 steps to the 0<sup>th</sup> level which has one way to the top. So at 2<sup>nd</sup> level we have two ways to the top.
- Similarly, with 1 step or 2 steps, we can climb to the previous first level or the previous second level, with memoization, we already have how many ways we can get to the top from these two levels, so we can sum up to get how many ways we can get to the top from current level.
- This is the Fibonacci series.
- Solve the Fibonacci series with dynamic programming method.


```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a
```

```python
class Solution2:
    def climbStairs(self, n: int) -> int:
        fib = [1] * 2
        for k in range(2,n + 1):
            fib[k%2] = fib[(k-1)%2] + fib[(k-2)%2]
        return fib[n%2]
```

The second one is much faster than the first one which actually takes more assignment operations. 


<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>
