
# [12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        integers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        letters = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        result = ''

        for i in reversed(range(len(integers))):
            f = num // integers[i]
            if f > 0:
                num = num % integers[i]
                result += f * letters[i]
            
            if num == 0:
                break

        return result
```

<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>
