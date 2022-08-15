## [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y, x0 = 0, x
        while x0 > 0:
            a, x0 = x0 % 10, x0 // 10
            y = 10 * y + a

        return x == y
```


<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>
