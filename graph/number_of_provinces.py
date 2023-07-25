from typing import List
from collections import deque

class Solution:
    # union find
    def findCircleNum2(self, isConnected: List[List[int]]) -> int:    
        edges = []

        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if isConnected[r][c] == 1:
                    edges.append([r,c])

        parent = [i for i in range(len(isConnected))]
        rank = [1]*len(isConnected)
        
        def find(n):
            p = parent[n]
            while p != parent[p]:
               parent[p] = parent[parent[p]]
               p = parent[p]
            return p

        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
               return 0
            if rank[p1] > rank[p2]:
               parent[p2] = p1
               rank[p1] += rank[p2]
            else:
               parent[p1] = p2
               rank[p2] += rank[p1]
            return 1
        
        res = len(isConnected)
        for i,j in edges:
            res -= union(i,j)
        
        return res

    # dfs
    # tc O(n^2), sc O(n^2)
    def findCircleNum3(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visit = set()
        res = 0

        def dfs(node):
            for neiNode, neiEdge in enumerate(isConnected[node]):
                if neiEdge == 1 and neiNode not in visit:
                    visit.add(neiNode)
                    dfs(neiNode)


        for i in range(N):
            if i not in visit:
                dfs(i)
                res += 1

        return res

    # bfs
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        if N in [0,1]:
            return N
        visitSet = set()
        res = 0

        for i in range(N):
            if i not in visitSet:
                q = deque([i])
                while q:
                    node = q.popleft()
                    if node not in visitSet:
                        visitSet.add(node)
                        for neiNode, neiEdge in enumerate(isConnected[node]):
                            if neiEdge == 1 and neiNode not in visitSet:
                                q.append(neiNode)
                
                res += 1

        return res