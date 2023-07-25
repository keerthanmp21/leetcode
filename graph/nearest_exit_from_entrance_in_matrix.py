from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        q = deque([entrance])
        visited = set(entrance)
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        steps = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r == 0 or c == 0 or r == ROWS-1 or c == COLS-1) and [r,c] != entrance:
                    return steps
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if 0<=row<ROWS and 0<=col<COLS and maze[row][col] == '.' and (row,col) not in visited:
                        visited.add((row,col))
                        q.append([row,col])
            steps += 1

        return -1
                