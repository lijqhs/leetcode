class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = dict()
        d2 = dict()

        for c in s:
            if c in d1:
                d1[c] = d1[c] + 1
            else:
                d1[c] = 1
            
        for c in t:
            if c in d2:
                d2[c] = d2[c] + 1
            else:
                d2[c] = 1

        for k, v in d1.items():
            if d2.get(k) == v:
                del d2[k]
            else:
                return False
        
        if len(d2) > 0:
            return False
        
        return True


class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = dict()
        d2 = dict()

        for i in range(len(s)):
            d1[s[i]] = 1 + d1.get(s[i], 0)
            d2[t[i]] = 1 + d2.get(t[i], 0)

        return d1 == d2

s = "rat"
t = "car"

s = "anagram"
t = "nagaram"


so = Solution1()
print(so.isAnagram(s,t))