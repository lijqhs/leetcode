# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = dict()
        d2 = dict()

        for i in range(len(s)):
            d1[s[i]] = 1 + d1.get(s[i], 0)
            d2[t[i]] = 1 + d2.get(t[i], 0)

        return d1 == d2
```


<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>
