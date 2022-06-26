import time

class Solution:
    """
    Manacher's algorithm
    https://en.wikipedia.org/wiki/Longest_palindromic_substring
    
    """
    def longestPalindrome(self, s: str) -> str:
        ss = ''.join(['|' + c for c in s] + ['|'])
        palinRadius = [0] * len(ss)

        ii = 0  # center index, iterating ss "|b|a|b|a|b|" when s "babab"
        radius = 0
        while ii < len(ss):
            while (ii - (radius+1) >= 0 and ii + (radius+1) < len(ss)) and (ss[ii - (radius+1)] == ss[ii + (radius+1)]):
                radius += 1

            palinRadius[ii] = radius

            oldCenter = ii
            oldRadius = radius
            ii = ii+1
            
            radius = 0 
            while ii <= oldCenter + oldRadius:
                mirroredCenter = oldCenter - (ii - oldCenter)
                maxMirroredRadius = oldCenter + oldRadius - ii
                if palinRadius[mirroredCenter] < maxMirroredRadius:
                    palinRadius[ii] = palinRadius[mirroredCenter]
                    ii = ii+1
                elif palinRadius[mirroredCenter] > maxMirroredRadius:
                    palinRadius[ii] = maxMirroredRadius
                    ii = ii+1
                else:
                    palinRadius[mirroredCenter] = maxMirroredRadius
                    radius = maxMirroredRadius # main while loop will start from here, expand the radius if elligible
                    break # exit while loop early

        max1 = max(palinRadius)
        index1 = [i for i, v in enumerate(palinRadius) if v == max1]

        print(palinRadius)
        print(index1)

        if index1:
            ii = index1[0]
            palinSS = ss[ii - (palinRadius[ii]):ii + (palinRadius[ii])+1]
            palinS = ''.join([c for c in palinSS if c != '|'])
            return palinS
            
        return ""




if __name__ == '__main__':
    s = Solution()
    start = time.time()
    
    # s.longestPalindrome('ababa')

    print(s.longestPalindrome('ababa'))
    print("cost time: " + str(time.time() - start))