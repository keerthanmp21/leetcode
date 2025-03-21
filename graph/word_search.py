from typing import List
from collections import deque

class Solution:
    # time complexity = O(ROWS * COLS * 4^(len(word)))
    # space complexity = O(len(word))
    def exist1(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        N = len(word)
        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        visited = set()

        def _dfs(r, c, i):
            if i == N:
                return True
            if( r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != word[i] or (r, c) in visited):
                return False

            visited.add((r,c))
            res = False
            for d in directions:
                res = res or _dfs(r + d[0], c + d[1], i+1)
            visited.remove((r,c))
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if _dfs(r, c, 0):
                    return True

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        N = len(word)
        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        
        
        def _bfs(row, col):
            q = deque([(row, col, 0, {(row, col)})])
            

            while q:
                r, c, i, visited = q.popleft()
                if i == N - 1:
                    return True
                for d in directions:
                    dr, dc = r + d[0], c + d[1]
                    if(0 <= dr < ROWS and 0 <= dc < COLS and
                    board[dr][dc] == word[i + 1] and
                    (dr, dc) not in visited):
                        q.append((dr, dc, i + 1, visited | {(dr, dc)}))

            return False


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and _bfs(r, c):
                    return True

        return False

    
