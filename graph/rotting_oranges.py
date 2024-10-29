from typing import List
from collections import deque


class Solution:
    # bfs
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh, time = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row < 0
                        or row == ROWS
                        or col < 0
                        or col == COLS
                        or grid[row][col] != 1
                    ):
                        continue
                    fresh -= 1
                    grid[row][col] = 2
                    q.append((row, col))
            time += 1

        return time if fresh == 0 else -1
    
'''
### Time Complexity

1. **Initialization of the Queue and Counting Fresh Oranges:**
   - You loop through each cell in the grid (of size ROWS * COLS), which takes 
   O(ROWS * COLS).

2. **Breadth-First Search (BFS) Traversal:**
   - The BFS processes each rotten orange and potentially each adjacent cell. In the 
   worst case, each fresh orange may be visited once as it becomes rotten.
   - Each cell in the grid can be processed once, leading to an additional time 
   complexity of O( ROWS * COLS).

Overall, the total time complexity is:
[O(ROWS * COLS)]

### Space Complexity

1. **Queue for BFS:**
   - The queue may store all rotten oranges, which can be at most O( ROWS * COLS) 
   in the worst case, particularly if the grid is filled with rotten oranges.

2. **Grid Space:**
   - The grid itself is already part of the input, so we typically do not count it 
   toward additional space complexity.

Overall, the space complexity is:
[O(ROWS * COLS)]

### Summary

- **Time Complexity:** O(ROWS * COLS)
- **Space Complexity:** O(ROWS * COLS)

'''
