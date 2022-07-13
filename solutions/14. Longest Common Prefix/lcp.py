from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i, j = 0, len(strs) - 1

        lcp = ""

        strs.sort()
        n = min(len(strs[i]), len(strs[j]))

        for d in range(n):
            if strs[i][d] != strs[j][d]:
                break
            lcp += strs[i][d]

        return lcp


class Solution2:
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



if __name__ == '__main__':

    s = Solution2()
    strs = ["flower","flow","flight"]
    strs = ["dog","racecar","car"]
    strs = ["a"]
    print(s.longestCommonPrefix(strs))

