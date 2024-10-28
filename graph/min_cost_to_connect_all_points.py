from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ptLen = len(points)
        adj_dict = defaultdict(list)
        for i in range(ptLen):
            x1, y1 = points[i]
            for j in range(i+1, ptLen):
                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                adj_dict[i].append([cost, j])
                adj_dict[j].append([cost,i])

        minHeap = [[0,0]]
        visited = set()
        res = 0

        while len(visited)<ptLen:
            cost, node1 = heapq.heappop(minHeap)
            if node1 in visited:
                continue
            res += cost
            visited.add(node1)
            for neiCost, nei in adj_dict[node1]:
                if nei not in visited:
                    heapq.heappush(minHeap,[neiCost, nei])
        
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