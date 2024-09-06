from typing import List

class Solution:
    # backtrack
    # tc = O(2^(m+n)), sc = O(m+n)
    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        def backtrack(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            if r < 0 or r >= m or c < 0 or c >= n or obstacleGrid[r][c]:
                return 0
            return backtrack(r + 1, c) + backtrack(r, c + 1)

        return backtrack(0, 0)

    # dp memoization
    # tc O(m*n), sc O(m*n)
    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        def backtrack(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            if r < 0 or r >= m or c < 0 or c >= n or obstacleGrid[r][c]:
                return 0
            if dp[r][c]:
                return dp[r][c]
            dp[r][c] = backtrack(r + 1, c) + backtrack(r, c + 1)
            return dp[r][c]

        return backtrack(0, 0)

    # dp tabulation
    # tc O(m*n), sc O(m*n)
    def uniquePathsWithObstacles3(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (
                    dp[i - 1][j] + dp[i][j - 1] if not obstacleGrid[i - 1][j - 1] else 0
                )
        return dp[-1][-1]

    # in-place
    # tc O(m*n), O(1)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] ^= 1
        for i in range(1, m):
            obstacleGrid[i][0] = obstacleGrid[i - 1][0] & (not obstacleGrid[i][0])

        for i in range(1, n):
            obstacleGrid[0][i] = obstacleGrid[0][i - 1] & (not obstacleGrid[0][i])

        for i in range(1, m):
            for j in range(1, n):
                obstacleGrid[i][j] = (
                    (obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1])
                    if not obstacleGrid[i][j]
                    else 0
                )

        return obstacleGrid[m - 1][n - 1]
