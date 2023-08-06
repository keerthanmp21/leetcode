from typing import List
from functools import cache

class Solution:
    # backtrack
    # tc O(2^n), sc O(n)
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        N = len(triangle)

        def dfs(i, j):
            if i == N:
                return 0
            lower_left = triangle[i][j] + dfs(i + 1, j)
            lower_right = triangle[i][j] + dfs(i + 1, j + 1)
            return min(lower_left, lower_right)

        return dfs(0, 0)

    # dp memoization
    # tc O(n^2), sc O(n^2)
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        dp = {}

        def dfs(i, j):
            if i == N:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            lower_left = triangle[i][j] + dfs(i + 1, j)
            lower_right = triangle[i][j] + dfs(i + 1, j + 1)
            dp[(i, j)] = min(lower_left, lower_right)
            return dp[(i, j)]

        return dfs(0, 0)

    # same as prev with inbuilt
    def minimumTotal3(self, triangle: List[List[int]]) -> int:
        N = len(triangle)

        @cache
        def dfs(i, j):
            if i == N:
                return 0
            lower_left = triangle[i][j] + dfs(i + 1, j)
            lower_right = triangle[i][j] + dfs(i + 1, j + 1)
            return min(lower_left, lower_right)

        return dfs(0, 0)

    # dp tabulation
    # tc O(n^2), sc O(n^2)
    def minimumTotal4(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        dp = [[-1] * N for _ in range(N)]
        dp[N - 1] = triangle[N - 1]
        for i in range(N - 2, -1, -1):
            for j in range(i + 1):
                lower_left = triangle[i][j] + dp[i + 1][j]
                lower_right = triangle[i][j] + dp[i + 1][j + 1]
                dp[i][j] = min(lower_left, lower_right)
        return dp[0][0]

    # dp tabulation
    # tc O(n^2), sc O(n)
    def minimumTotal5(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i + 1])

        return dp[0]
