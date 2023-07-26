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