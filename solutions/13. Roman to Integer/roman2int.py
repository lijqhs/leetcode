class Solution:
    def romanToInt(self, s: str) -> int:
        integers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        letters = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        result = 0

        i = len(letters) - 1
        while i >= 0:
            if s[0:len(letters[i])] == letters[i]:
                result += integers[i]
                s = s[len(letters[i]):]
            else:
                i -= 1

        return result

so = Solution()
s = "III"
s = "MCMXCIV"
print(so.romanToInt(s))