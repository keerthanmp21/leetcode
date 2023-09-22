class Solution:
    # backtracking, brute force, recursion
    # tc O(n^2), sc O(n)
    def climbStairs1(self, n: int) -> int:
        def backtrack(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return backtrack(n - 1) + backtrack(n - 2)

        return backtrack(n)

    # dp memoization
    # tc O(n), sc O(n)
    def climbStairs2(self, n: int) -> int:
        dp = {1: 1, 2: 2}

        def backtrack(n):
            if n in dp:
                return dp[n]
            dp[n] = backtrack(n - 1) + backtrack(n - 2)
            return dp[n]

        return backtrack(n)

    # dp tabulation
    # time O(n) space O(n)
    def climbStairs3(self, n: int) -> int:
        if n in [0, 1, 2]:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    # greedy
    # time O(n) space O(1)
    def climbStairs4(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
