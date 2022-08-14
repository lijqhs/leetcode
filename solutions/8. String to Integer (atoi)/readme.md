
# [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        sign, n, digitOn = 1, 0, False
        MIN, MAX = -2**31, 2**31 - 1

        for i in range(len(s)):
            if digitOn and (s[i] < '0' or s[i] > '9'):
                break
            if not digitOn:
                if s[i] == ' ':
                    continue
                elif s[i] == '-':
                    sign, digitOn = -1, True
                elif s[i] == '+':
                    digitOn = True
                    continue
                elif s[i] < '0' or s[i] > '9':
                    break
            if s[i] >= '0' and s[i] <= '9':
                digitOn = True
                digit = ord(s[i]) - ord('0')
                if n > MAX // 10 or (n == MAX // 10 and digit > MAX % 10):
                    return MAX if sign == 1 else MIN
                n *= 10
                n += digit

        return n * sign
```

<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>
