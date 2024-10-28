from typing import List
from collections import defaultdict, deque

class Solution:
    #dfs
    def validPath2(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adj_dict = defaultdict(list)
        for edge in edges:
            adj_dict[edge[0]].append(edge[1])
            adj_dict[edge[1]].append(edge[0])
        
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if node == destination:
                return True
            visited.add(node)
            for nei in adj_dict[node]:
                if dfs(nei):
                    return True
            return False

        return dfs(source)
        
    #bfs
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    
        adj_dict = defaultdict(list)
        for edge in edges:
            adj_dict[edge[0]].append(edge[1])
            adj_dict[edge[1]].append(edge[0])

        q = deque([source])
        visited = set([source])

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for nei in adj_dict[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        
        return False


'''

### (DFS)

**Time Complexity:**
- In the worst case, the DFS explores all nodes and edges. 
- The time complexity is \(O(V + E)\), where \(V\) is the number of vertices (nodes) 
and \(E\) is the number of edges. This is because each node and edge is processed once.

**Space Complexity:**
- The space complexity primarily comes from the recursion stack and the visited set.
- The maximum depth of the recursion can go up to \(O(V)\) in the worst case (if the 
graph is a linear chain).
- The visited set also requires \(O(V)\) space.
- Thus, the overall space complexity is \(O(V)\).

### `validPath` (BFS)

**Time Complexity:**
- Similar to DFS, in the worst case, BFS also explores all nodes and edges.
- The time complexity is \(O(V + E)\).

**Space Complexity:**
- The space complexity for BFS comes from the queue and the visited set.
- The queue can hold up to \(O(V)\) nodes in the worst case.
- The visited set requires \(O(V)\) space as well.
- Therefore, the overall space complexity is \(O(V)\).

### Summary

- **`validPath1` (DFS):**
  - Time Complexity: \(O(V + E)\)
  - Space Complexity: \(O(V)\)

- **`validPath` (BFS):**
  - Time Complexity: \(O(V + E)\)
  - Space Complexity: \(O(V)\)
'''