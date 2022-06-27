class Solution:
    def isPalindrome(self, x: int) -> bool:
        y, x0 = 0, x
        while x0 > 0:
            a, x0 = x0 % 10, x0 // 10
            y = 10 * y + a

        return x == y


if __name__ == '__main__':
    # s = '   -114748364'
    x = 121
    solution = Solution()
    print(solution.isPalindrome(x))
