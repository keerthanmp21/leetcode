class Solution:
    # recursion
    # tc O(3^n), sc O(n)
    def tribonacci1(self, n: int) -> int:
        def recursion(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            return recursion(n - 1) + recursion(n - 2) + recursion(n - 3)

        return recursion(n)

    # dp memoization
    # tc (n^3), sc O(n)
    def tribonacci2(self, n: int) -> int:
        dp = {0: 0, 1: 1, 2: 1}

        def recursion(n):
            if n in dp:
                return dp[n]
            dp[n] = recursion(n - 1) + recursion(n - 2) + recursion(n - 3)
            return dp[n]

        return recursion(n)

    # dp tabulation
    # tc O(n), sc O(n)
    def tribonacci3(self, n: int) -> int:
        dp = {0: 0, 1: 1, 2: 1}
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]
