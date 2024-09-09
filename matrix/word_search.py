from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        N = len(word)
        visited = set()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(r, c, i):
            if i == N:
                return True
            if (r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or board[r][c] != word[i]):
                return False

            visited.add((r,c))
            res = False
            for d in directions:
                res = res or dfs(r + d[0], c + d[1], i+1)
            visited.remove((r,c))
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False