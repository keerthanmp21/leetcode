from functools import cache


class Solution:
    # backtrack
    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:
        def backtrack(i, j, k):
            if i < 0 and j < 0 and k < 0:
                return True
            if i >= 0 and s1[i] == s3[k] and j >= 0 and s2[j] == s3[k]:
                return backtrack(i - 1, j, k - 1) or backtrack(i, j - 1, k - 1)
            elif i >= 0 and s1[i] == s3[k]:
                return backtrack(i - 1, j, k - 1)
            elif j >= 0 and s2[j] == s3[k]:
                return backtrack(i, j - 1, k - 1)
            return False

        return backtrack(len(s1) - 1, len(s2) - 1, len(s3) - 1)

    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def backtrack(i, j, k):
            if i < 0 and j < 0 and k < 0:
                return True
            if i >= 0 and s1[i] == s3[k] and j >= 0 and s2[j] == s3[k]:
                return backtrack(i - 1, j, k - 1) or backtrack(i, j - 1, k - 1)
            elif i >= 0 and s1[i] == s3[k]:
                return backtrack(i - 1, j, k - 1)
            elif j >= 0 and s2[j] == s3[k]:
                return backtrack(i, j - 1, k - 1)
            return False

        return backtrack(len(s1) - 1, len(s2) - 1, len(s3) - 1)

    def isInterleave3(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
