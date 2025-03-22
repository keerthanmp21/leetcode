from typing import List
from collections import defaultdict
import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, num):
        while num != self.parent[num]:
            self.parent[num] = self.parent[self.parent[num]]
            num = self.parent[num]
        return num

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False  # Already connected

        if self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        elif self.rank[rootB] > self.rank[rootA]:
            self.parent[rootA] = rootB
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1
        
        return True

class Solution:
    # time complexity O(N² log N)
    def minCostConnectPoints1(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        N = len(points)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append([j, cost])
                adjList[j].append([i, cost])

        minHeap = [[0, 0]]
        res = 0
        visited = set()

        while len(visited) < N:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for neiNode, neiCost in adjList[node]:
                if neiNode not in visited:
                    heapq.heappush(minHeap, [neiCost, neiNode])

        return res

    # time complexity O(N² log N)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = []

        # Create all edges with their Manhattan distance as weight
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                edges.append((cost, i, j))

        # Sort edges based on cost
        edges.sort()
        uf = UnionFind(N)
        res, count = 0, 0

        # Kruskal’s Algorithm
        for cost, u, v in edges:
            if uf.union(u, v):  # If successfully connected
                res += cost
                count += 1
                if count == N - 1:  # Minimum Spanning Tree formed
                    break

        return res
    
'''

### Time Complexity

1. **Building the Adjacency List:**
   - The adjacency list is built using a nested loop where each point is compared with
     every other point. This results in \(O(N^2)\) operations, where \(N\) is the 
     number of points.
   - The cost to connect two points is computed in constant time \(O(1)\).
   - Thus, constructing the adjacency list takes \(O(N^2)\).

2. **Using Prim's Algorithm with a Min-Heap:**
   - The main loop runs while there are nodes to process, which can happen up to \(N\)
      times since we want to visit all nodes.
   - Each node may also push its edges into the heap. In the worst case, all edges 
   will be processed, which is \(O(E)\) where \(E\) can be up to \(O(N^2)\) in a 
   complete graph.
   - The operations with the heap (insert and remove) take \(O(\log N)\). Thus, the 
   overall complexity for processing the heap in the worst case becomes \(O(E \log N)\).

### Overall Time Complexity
- Combining both parts, the total time complexity is dominated by the adjacency list 
construction:
  [ O(N^2) + O(E \log N) ~= O(N^2) {(since } E { can be up to } O(N^2)  as well)}]

### Space Complexity

1. **Adjacency List:**
   - The adjacency list will store at most \(O(N^2)\) entries since every point can be
     connected to every other point.
   
2. **Min-Heap:**
   - The min-heap will store at most \(O(N)\) nodes in the worst case, as it holds 
   nodes that are waiting to be processed.

3. **Visited Set:**
   - The visited set will also hold up to \(O(N)\) nodes.

### Overall Space Complexity
- The overall space complexity is thus:
  \[
  O(N^2) {(from the adjacency list)}
  \]

### Summary

- **Time Complexity:** \(O(N^2)\)
- **Space Complexity:** \(O(N^2)\)

'''