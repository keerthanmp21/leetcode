class Solution:
    # two pointers
    # tc O(n^2), sc O(1)
    def longestPalindrome1(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

    # brute force
    # tc O(n^3), sp O(1)
    def longestPalindrome2(self, s: str) -> str:
        N = len(s)
        startingIndex = 0
        maxLen = 0

        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPali(i, j):
                    if (j - i + 1) > maxLen:
                        maxLen = j - i + 1
                        startingIndex = i

        return s[startingIndex : startingIndex + maxLen]

    # dp tabulation (bottom up) iterative
    # tc O(n^2), sc O(n^2)
    def longestPalindrome3(self, s: str) -> str:
        N = len(s)
        # dp = [[False]*N]*N
        dp = [[False] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = True
        res = s[0]

        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if len(s[i : j + 1]) > len(res):
                            res = s[i : j + 1]

        return res
