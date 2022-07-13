class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        starState = False
        prevState = ''

        i = 0 # index of str
        j = 0 # index of patter
        while j < len(p):
            # print(p[j], s[i])
            # print(starState)
            if j < len(p) - 1 and p[j + 1] == "*":
                starState = True
            else:
                starState = False
            
            if starState:
                c = p[j] # should appear 0 or more
                while i < len(s) and (s[i] == c or c == '.'):
                    i += 1
                # now s[i] is not c, move to next
                j += 2
                if i == len(s):
                    if j == len(p):
                        return True
                    else:
                        return False
                starState = False
            else:
                if p[j] == s[i] or p[j] == '.':
                    i += 1
                    j += 1
                    if i == len(s):
                        if j == len(p):
                            return True
                        else:
                            return False
                else:
                    return False
            
        return False
            


if __name__ == '__main__':
    s = "ab"
    p = ".*"

    # s="aab"
    # p="c*a*b"
    
    solution = Solution()
    print(solution.isMatch(s, p))
