# backtracking
# tc O(3^n), sc O(1)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        ROWS = len(matrix)
        COLS = len(matrix[0])
        res = 0

        def backtrack(r,c):
            if r >= ROWS or c >= COLS:
                return 0
            if matrix[r][c] == '0':
                return 0
            down = backtrack(r+1,c)
            right = backtrack(r,c+1)
            diag = backtrack(r+1,c+1)
            return 1+min(down,right,diag)
            
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, backtrack(r,c))
        return res*res
        
# dp memoization
# tc O(n^3), sc O(n)
class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        ROWS = len(matrix)
        COLS = len(matrix[0])
        res = 0
        dp = {}
        def backtrack(r,c):
            if r >= ROWS or c >= COLS:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            if matrix[r][c] == '0':
                dp[(r,c)] = 0
                return dp[(r,c)]
            down = backtrack(r+1,c)
            right = backtrack(r,c+1)
            diag = backtrack(r+1,c+1)
            dp[(r,c)] = 1+min(down,right,diag)
            return dp[(r,c)]
            
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, backtrack(r,c))
        return res*res

# dp tabulation
# tc O(m*n), sc O(m*n)    
class Solution3:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        ROWS = len(matrix)
        COLS = len(matrix[0])
        res = 0
        dp = [[0]*(COLS+1) for _ in range(ROWS+1)]
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                    res = max(res, dp[r+1][c+1])
        return res*res







        