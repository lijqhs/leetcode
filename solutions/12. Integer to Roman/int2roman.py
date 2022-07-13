class Solution:
    def intToRoman(self, num: int) -> str:
        # I             1
        # V             5
        # X             10
        # L             50
        # C             100
        # D             500
        # M             1000

        # I can be placed before V (5) and X (10) to make 4 and 9. 
        # X can be placed before L (50) and C (100) to make 40 and 90. 
        # C can be placed before D (500) and M (1000) to make 400 and 900.

        # letters = {
        #     1: 'I',
        #     4: 'IV',
        #     5: 'V',
        #     9: 'IX',
        #     10: 'X',
        #     40: 'XL',
        #     50: 'L',
        #     90: 'XC',
        #     100: 'C',
        #     400: 'CD',
        #     500: 'D',
        #     900: 'CM',
        #     1000: 'M'
        # }

        integers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        letters = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        result = ''

        for i in reversed(range(len(integers))):
            f = num // integers[i]
            if f > 0:
                num = num % integers[i]
                result += f * letters[i]
            
            if num == 0:
                break

        return result

s = Solution()
s.intToRoman(4)