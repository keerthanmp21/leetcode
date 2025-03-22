from typing import List
from collections import deque

from typing import List
from collections import deque

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n  # Rank to optimize union

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

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

    # time complexity O(n^2)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        uf = UnionFind(N)

        # Process adjacency matrix and unite connected nodes
        for i in range(N):
            for j in range(i + 1, N):  # Avoid redundant checks (upper triangle)
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        
        # Count unique provinces by checking root parents
        return len(set(uf.find(i) for i in range(N)))
