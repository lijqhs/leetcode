import time

class Solution:
    """
    Manacher's algorithm
    https://en.wikipedia.org/wiki/Longest_palindromic_substring
    
    slow version
    """
    def longestPalindrome(self, s: str) -> str:
        ss = ''.join(['|' + c for c in s] + ['|'])
        palinRadius = [0] * len(ss)

        ii = 0  # center index, iterating ss "|b|a|b|a|b|" when s "babab"
        while ii < len(ss):
            radius = 0
            while (ii - (radius+1) >= 0 and ii + (radius+1) < len(ss)) and (ss[ii - (radius+1)] == ss[ii + (radius+1)]):
                radius += 1

            palinRadius[ii] = radius
            ii += 1
        
        max1 = max(palinRadius)
        index1 = [i for i, v in enumerate(palinRadius) if v == max1]

        if index1:
            ii = index1[0]
            palinSS = ss[ii - (palinRadius[ii]):ii + (palinRadius[ii])+1]
            palinS = ''.join([c for c in palinSS if c != '|'])
            return palinS

        return ""


        # print(palinRadius)
        # print(index1)

        # palinSubstring = []
        # for ii in index1:
        #     palinSS = ss[ii - (palinRadius[ii]):ii + (palinRadius[ii])+1]
        #     palinS = ''.join([c for c in palinSS if c != '|'])
        #     palinSubstring.append(palinS)

        # print(palinSubstring)

        # return len(palinSubstring) > 0 and palinSubstring[0] or []



if __name__ == '__main__':
    s = Solution()
    start = time.time()
    
    # s.longestPalindrome('ababa')

    print(s.longestPalindrome('a'))
    print("cost time: " + str(time.time() - start))