class Solution:
    # backtrack
    # tc O(2^n), sc O(n)
    def numDecodings1(self, s: str) -> int:
        N = len(s)

        def backtrack(idx):
            if idx == N:
                return 1
            if s[idx] == "0":
                return 0
            res = backtrack(idx + 1)  # single digit
            if idx < N - 1 and (
                s[idx] == "1" or (s[idx] == "2" and s[idx + 1] in "0123456")
            ):  # two digit
                res += backtrack(idx + 2)
            return res

        return backtrack(0)

    # dp memoization
    # tc O(n), sp O(n)
    def numDecodings2(self, s: str) -> int:
        N = len(s)
        if N == 0:
            return 0
        dp = [-1] * N

        def backtrack(idx):
            if idx == N:
                return 1
            if s[idx] == "0":
                return 0
            if dp[idx] != -1:
                return dp[idx]
            res = backtrack(idx + 1)
            if idx < N - 1 and (
                s[idx] == "1" or (s[idx] == "2" and s[idx + 1] in "0123456")
            ):
                res += backtrack(idx + 2)
            dp[idx] = res
            return dp[idx]

        return backtrack(0)

    # dp tabulation
    # tc O(n), sc O(n)
    def numDecodings3(self, s: str) -> int:
        N = len(s)
        dp = {N: 1}

        for i in range(N - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if (i + 1) < N and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]

        return dp[0]
