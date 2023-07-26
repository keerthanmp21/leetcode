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


