from typing import List
from collections import deque


class Solution:
    # dfs
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        res = []
        safe = {}

        def dfs(node):
            if node in safe:
                return safe[node]
            safe[node] = False
            # if there is no nei then it is safe
            # or if all nei nodes are safe then it is safe
            for neiNode in graph[node]:
                if not dfs(neiNode):
                    return False
            safe[node] = True
            return True

        for node in range(n):
            if dfs(node):
                res.append(node)

        return res

    # bfs(topological sort)
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        indegree_edges = [[] for i in range(N)]
        outdegree = [0] * N

        for i in range(N):
            outdegree[i] = len(graph[i])
            for j in graph[i]:
                indegree_edges[j].append(i)
        
        q = deque()
        res = [] * N
        for node in range(N):
            if outdegree[node] == 0:
                q.append(node)

        while q:
            cur_node = q.popleft()
            res.append(cur_node)
            for nei_node in indegree_edges[cur_node]:
                if outdegree[nei_node] != 0:
                    outdegree[nei_node] -= 1
                if outdegree[nei_node] == 0:
                    q.append(nei_node)

        return sorted(res)