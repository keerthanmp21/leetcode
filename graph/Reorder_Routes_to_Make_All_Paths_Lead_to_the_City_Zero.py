from typing import List
from collections import deque, defaultdict

class Solution:
    # dfs
    def minReorder2(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a,b) for a,b in connections}
        neighbors = {city:[] for city in range(n)}
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        visited = set([0])
        changes = [0]

        def dfs(city):
            for nei in neighbors[city]:
                if nei in visited:
                    continue
                if (nei, city) not in edges:
                    changes[0] += 1
                visited.add(nei)
                dfs(nei)

        dfs(0)
        return changes[0]

    # bfs
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = defaultdict(list)
        for src, dest in connections:
            edges[src].append((dest, 1))
            edges[dest].append((src, 0))
        
        q = deque([0])
        visited = set([0])
        changes = 0
        
        while q:
            curr = q.popleft()
            for neiCity, cost in edges[curr]:
                if neiCity not in visited:
                    visited.add(neiCity)
                    changes += cost
                    q.append(neiCity)
                    
        return changes
    
'''

### (DFS)

**Time Complexity:**
1. **Building the Neighbors Dictionary:**
   - Constructing the `neighbors` dictionary takes \(O(n + m)\), where \(n\) is the 
   number of cities and \(m\) is the number of connections.
2. **DFS Traversal:**
   - The DFS visits each node once, leading to a time complexity of \(O(n + m)\).

Overall, the time complexity is:
O(n + m)

**Space Complexity:**
1. **Neighbors Dictionary:**
   - The neighbors dictionary uses \(O(n + m)\) space.
2. **Visited Set:**
   - The visited set uses \(O(n)\) space.
3. **Recursion Stack:**
   - The maximum depth of the recursion can go up to \(O(n)\) in the worst case.

Overall, the space complexity is:
O(n + m)

### (BFS)

**Time Complexity:**
1. **Building the Edges Dictionary:**
   - Similar to the first method, constructing the edges dictionary takes \(O(n + m)\).
2. **BFS Traversal:**
   - The BFS processes each node once and examines each edge, leading to a time
     complexity of \(O(n + m)\).

Overall, the time complexity is:
O(n + m)

**Space Complexity:**
1. **Edges Dictionary:**
   - The edges dictionary uses \(O(n + m)\) space.
2. **Visited Set:**
   - The visited set uses \(O(n)\) space.
3. **Queue for BFS:**
   - The queue can store up to \(O(n)\) nodes in the worst case.

Overall, the space complexity is:
O(n + m)
### Summary

For both methods:

- **Time Complexity:** \(O(n + m)\)
- **Space Complexity:** \(O(n + m)\)

'''