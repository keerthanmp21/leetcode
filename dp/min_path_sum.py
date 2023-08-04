from typing import List

class Solution:
    # brute force or backtrack
    # tc O(2^(m*n))
    def minPathSum1(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        def backtrack(r,c):
            if r == 0 and c == 0:
                return grid[r][c]
            if r == 0: # reached first row then move horizont
                return grid[r][c]+backtrack(r,c-1)
            if c == 0: # reached first col then move vertical
                return grid[r][c]+backtrack(r-1,c)
            return grid[r][c]+min(backtrack(r-1,c),backtrack(r,c-1))

        return  backtrack(ROWS-1, COLS-1)

    # dp memoization
    # tc O(m*n), sc O(m*n)
    def minPathSum2(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dp = {}
        def backtrack(r,c):
            if r == 0 and c == 0:
                return grid[r][c]
            if (r,c) in dp:
                return dp[(r,c)]
            if r == 0:
                dp[(r,c)] = grid[r][c]+backtrack(r,c-1)
                return dp[(r,c)]
            if c == 0:
                dp[(r,c)] = grid[r][c]+backtrack(r-1,c)
                return dp[(r,c)]
            dp[(r,c)] = grid[r][c]+min(backtrack(r-1,c),backtrack(r,c-1))
            return dp[(r,c)]
        return backtrack(ROWS-1, COLS-1)

        #dp tabulation
        # tc O(m*n), sc O(1)
    def minPathSum3(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if r==0 and c==0:
                    pass
                elif r==0 and c!=0:
                    grid[r][c] = grid[r][c] + grid[r][c-1]
                elif r!=0 and c==0:
                    grid[r][c] = grid[r][c] + grid[r-1][c]
                else:
                    grid[r][c] = grid[r][c]+min(grid[r][c-1],grid[r-1][c])
        return grid[ROWS-1][COLS-1]







