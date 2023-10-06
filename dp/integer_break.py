from functools import cache


class Solution:
    def integerBreak1(self, n: int) -> int:
        if n <= 3:
            return n - 1
        @cache
        def dp(num):
            if num <= 3:
                return num

            max_val = num
            for i in range(2, num):
                max_val = max(max_val, i * dp(num-i))

            return max_val

        return dp(n)

    # dp
    # tc O(n^2), sc O(n)
    def integerBreak2(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0] * (n + 1)
        dp[1], dp[2], dp[3] = 1, 2, 3

        # Fill the dynamic programming table for larger numbers
        for num in range(4, n + 1):
            max_val = num
            for i in range(2, num):
                max_val = max(max_val, i * dp[num - i])
            dp[num] = max_val

        return dp[n]

    # math
    # tc O(n), O(1)
    def integerBreak3(self, n: int) -> int:
        if n <= 3:
            return n - 1

        res = 1
        while n > 4:
            res *= 3
            n -= 3

        return res * n