class Solution:
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        def backtrack(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + backtrack(i + 1, j + 1)
            else:
                return max(backtrack(i + 1, j), backtrack(i, j + 1))

        return backtrack(0, 0)

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        dp = {}
        def backtrack(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + backtrack(i + 1, j + 1)
            else:
                dp[(i, j)] = max(backtrack(i + 1, j), backtrack(i, j + 1))
            return dp[(i, j)]

        return backtrack(0, 0)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0 for j in range(N + 1)] for i in range(M + 1)]

        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]