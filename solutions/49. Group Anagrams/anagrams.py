
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        count = {}

        for s in strs:
            d = {} # char counts
            for c in s:
                d[c] = 1 + d.get(c, 0)
            
            found = False
            for k, v in count.items():
                if d == v:
                    group[k] = group[k] + [s]
                    found = True

            if not found:
                count[s] = d
                group[s] = [s]

        return list(group.values())


class Solution1:
    """
    use radix sort
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            ss = self.radixsort(s)
            group[ss] = [s] + group.get(ss, [])
            
        return list(group.values())


    def radixsort(self, s: str) -> str:
        R = 26 # number of lower case letters
        a = ord('a') # ascii for 'a'
        ss = [''] * len(s) # ordered str
        count = [0] * (R + 1)
        for c in s:
            count[ord(c)-a+1] = count[ord(c)-a+1] + 1

        # print(count)
        
        for r in range(R):
            count[r+1] = count[r] + count[r+1]
        
        # print(count)
        
        for c in s:
            ss[count[ord(c)-a]] = c
            count[ord(c)-a] = count[ord(c)-a] + 1   # for duplicate chars
        
        # print(count)
        
        return ''.join(ss)
        


class Solution2:
    """
    use defaultdict
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            count = [0] * 26 # count for 26 letters
            for c in s:
                count[ord(c)-ord('a')] += 1
            d[tuple(count)].append(s)

        return d.values()


class Solution3:
    """
    use sorted
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            ss = ''.join(sorted(s))
            group[ss].append(s)
            
        return list(group.values())




strs = ["eat","tea","tan","ate","nat","bat"]
# strs = ["a"]
# strs = [""]
s = Solution3()
print(s.groupAnagrams(strs))
# print(s.radixsort("hello"))