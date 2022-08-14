
# [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = x < 0 and -1 or 1
        r = str(x * sign)[::-1]
        return 0 if (len(r) == 10 and r > str(2**31)) else int(r) * sign
```

<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>
