from typing import List
from collections import deque

class Solution:
    # dfs
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return safe[i]
            safe[i] = True
            return safe[i]
        
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
                
        return res
    
    # bfs(topological sort)
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        edges = [[] for i in range(N)]
        indegree = [0]*N
        
        for i in range(N):
            indegree[i] = len(graph[i])
            for j in graph[i]:
                edges[j].append(i)

        q = deque()
        res = []*N
        for i in range(N):
            if indegree[i] == 0:
                q.append(i)

        while q:
            u=q.popleft()
            res.append(u)
            for i in edges[u]:
                if indegree[i] != 0:
                    indegree[i]-=1
                if indegree[i] == 0:
                    q.append(i)
                    

        return sorted(res)
    
s = Solution()
print(s.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))