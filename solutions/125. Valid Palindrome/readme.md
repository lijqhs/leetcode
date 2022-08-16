## [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

Start from two ends of the string and skip every non-alphanumeric characters.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1

        s = s.lower()
        
        while i < j:
            while (i < len(s) and not self.isAlphanumeric(s[i])): i += 1
            while (j > 0 and not self.isAlphanumeric(s[j])): j -= 1

            if i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False

        return True


    def isAlphanumeric(self, c):
        # number ASCII: 48-57
        # letter lowercase: 97-122

        code = ord(c)
        return (code >= 48 and code <= 57) or \
            (code >= 97 and code <= 122)


s = "A man, a plan, a canal: Panama"
s = "race a car"
s = "a*  ."
so = Solution()
print(so.isPalindrome(s))
```