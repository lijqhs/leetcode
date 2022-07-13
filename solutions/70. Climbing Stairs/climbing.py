class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a


class Solution2:
    def climbStairs(self, n: int) -> int:
        fib = [1] * 2
        for k in range(2,n + 1):
            fib[k%2] = fib[(k-1)%2] + fib[(k-2)%2]
        return fib[n%2]


if __name__ == '__main__':
    s = Solution2()
    print(s.climbStairs(10))