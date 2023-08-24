from typing import List
import heapq

class Solution:
    # dijkstra (bfs using minheap)
    def swimInWater1(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minH = [[grid[0][0], 0, 0]]
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for d in directions:
                neiR, neiC = r + d[0], c + d[1]
                if (
                    (neiR < 0 or neiR == N)
                    or (neiC < 0 or neiC == N)
                    or (neiR, neiC) in visited
                ):
                    continue
                visited.add((neiR, neiC))
                maxT = max(t, grid[neiR][neiC])
                heapq.heappush(minH, [maxT, neiR, neiC])

    def swimInWater2(self, grid: List[List[int]]) -> int:
        N = len(grid)
        low, high = grid[0][0], N * N - 1

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, waterHeight):
            if (
                (r < 0 or r == N)
                or (c < 0 or c == N)
                or (r, c) in visited
                or grid[r][c] > waterHeight
            ):
                return False
            visited.add((r, c))
            if r == N - 1 and c == N - 1:
                return True
            for d in directions:
                dr, dc = r + d[0], c + d[1]
                if (
                    (dr < 0 or dr == N)
                    or (dc < 0 or dc == N)
                    or (dr, dc) in visited
                    or grid[dr][dc] > waterHeight
                ):
                    continue
                if dfs(dr, dc, waterHeight):
                    return True
            return False

        while low < high:
            mid = low + (high - low) // 2
            visited = set()
            if dfs(0, 0, mid):
                high = mid
            else:
                low = mid + 1

        return low
