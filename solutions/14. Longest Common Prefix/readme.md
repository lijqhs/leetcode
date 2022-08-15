## [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""

        lcp = ""
        s1 = min(strs)
        s2 = max(strs)

        n = min(len(s1), len(s2))

        for d in range(n):
            if s1[d] != s2[d]:
                break
            lcp += s1[d]

        return lcp
```


<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>
