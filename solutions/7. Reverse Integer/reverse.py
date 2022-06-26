class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0

        s = negative and str(-x) or str(x)  # digit part

        N = 2**31
        low = str(int(N))      # lower bound digit part
        high = str(int(N-1))

        reversedS = s[::-1]

        if len(reversedS) == len(high):
            if negative:
                i = 0
                while i < len(reversedS):
                    if reversedS[i] < low[i]:
                        break
                    if reversedS[i] > low[i]:
                        return 0
                    i += 1
            else:
                i = 0
                while i < len(reversedS):
                    if reversedS[i] < high[i]:
                        break
                    if reversedS[i] > high[i]:
                        return 0
                    i += 1
        
        result = int(reversedS)

        return negative and -result or result


class Solution2:
    def reverse(self, x: int) -> int:
        sign = x < 0 and -1 or 1
        r = str(x * sign)[::-1]
        return 0 if (len(r) == 10 and r > str(2**31)) else int(r) * sign



if __name__ == '__main__':
    x = -114748364
    solution = Solution2()
    print(solution.reverse(x))
