## [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

```python
from typing import List
from collections import defaultdict, OrderedDict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for i in nums:
            d[i] += 1

        return list(OrderedDict(sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]).keys())
```



<br/>
<div align="right">
    <b><a href="#top">↥ back to top</a></b>
</div>
<br/>
