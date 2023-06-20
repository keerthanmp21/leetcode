#backtracking
# tc = O(2^(m+n)), sc = O(m+n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(r,c):
            if r == m-1 or c == n-1:
                return 1
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            
            return helper(r+1,c) +helper(r,c+1)
        return helper(0,0)

# dp top down, memoization
# time O(m*n), space O(m*n)
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    
        def helper(r,c):
            if r == m-1 or c == n-1:
                return 1
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            dp[r][c] = helper(r+1,c) +helper(r,c+1)
            return dp[r][c]
        
        return helper(0,0)   

#dp tabulation
#tc = O(m*n), sc = O(m*n)
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]