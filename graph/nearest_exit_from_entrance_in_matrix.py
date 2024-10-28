from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        q = deque([entrance])
        visited = set(entrance)
        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]

        steps = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1) and [r, c] != entrance:
                    return steps
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < ROWS and 0 <= col < COLS and maze[row][col] == '.' and (row, col) not in visited:
                        visited.add((row, col))
                        q.append([row, col])
            steps += 1

        return -1
                

'''

### Time Complexity

1. **Traversal of the Maze:**
   - The BFS algorithm explores each cell in the maze. In the worst case, you may need 
   to visit every cell.
   - Let \( R \) be the number of rows and \( C \) be the number of columns. The total 
   number of cells is \( R \times C \).

2. **Checking Valid Moves:**
   - For each cell, the algorithm checks up to 4 possible directions (up, down, left, 
   right).
   - Therefore, the time complexity is \( O(R \times C) \).

### Space Complexity

1. **Queue for BFS:**
   - In the worst case, the queue can hold all cells in the maze, which is \( O(R 
   \times C) \).
   - The queue stores the positions of the cells that are being processed.

2. **Visited Set:**
   - The visited set also stores the coordinates of each cell visited, leading to 
   \( O(R \times C) \) space usage in the worst case.

### Summary

- **Time Complexity:** \( O(R \times C) \)
- **Space Complexity:** \( O(R \times C) \)

'''