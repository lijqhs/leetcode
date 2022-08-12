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

s = "anagram"
t = "nagaram"

s = "rat"
t = "car"

so = Solution()
print(so.isAnagram(s,t))