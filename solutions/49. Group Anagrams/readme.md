## [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            ss = ''.join(sorted(s))
            group[ss].append(s)
            
        return list(group.values())
```

In this case, `defaultdict` is much more efficient than `dict`.


<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>
