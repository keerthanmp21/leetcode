from typing import List
from collections import deque, defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)}
        self.rank = {i: 0 for i in range(1, n + 1)}

    def find(self, num):
        while num != self.parent[num]:
            self.parent[num] = self.parent[self.parent[num]]
            num = self.parent[num]
        return num # self.parent[num]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False # cycle detected

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

        return True

class Solution:
    # union find
    # time O(n), space O(n)
    def findRedundantConnection1(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        weight = [1 for i in range(len(edges) + 1)]

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]] # path compression (it is an option), grandfather
                p = parent[p]
            return p   

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if weight[p2] > weight[p1]:
                parent[p1] = p2
                weight[p2] += weight[p1]
            else:
                parent[p2] = p1
                weight[p1] += weight[p2]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1,n2]


    # dfs
    # time O(n^2), space O(n^2)
    def findRedundantConnection2(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        edges_list = defaultdict(list)
        
        def dfs(src, dest):
            # if a node is visited we cannot find a path through it as it itself formed a cycle which we do not want
            if src in visitSet:
                return False
            if src == dest:
                return True
            visitSet.add(src)
            for node in edges_list[src]:
                if dfs(node, dest):
                    return True
            return False

        for src, dest in edges:
            visitSet = set()
            # perform dfs every time you add an edge
			# so that we if a cycle is formed we know exactly this edge has caused the cycle
            if dfs(src, dest):
                return [src, dest]
            edges_list[src].append(dest)
            edges_list[dest].append(src)

        return []

    # bfs
    # time O(n^2), space O(n^2)
    def findRedundantConnection3(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        edges_list = defaultdict(list)

        def bfs(src, dest):
            q = deque([src])
            visitSet = set([src])
            while q:
                curNode = q.popleft()
                if curNode == dest:
                    return True
                for neiNode in edges_list[curNode]:
                    if neiNode not in visitSet:
                        visitSet.add(neiNode)
                        q.append(neiNode)

            return False



        for src, dest in edges:
            visitSet = set()
            # perform bfs every time you add an edge
			# so that we if a cycle is formed we know exactly this edge has caused the cycle
            if bfs(src, dest):
                return [src, dest]
            edges_list[src].append(dest)
            edges_list[dest].append(src)

        return []

    # Time Complexity: O(N) (almost constant due to path compression).
    # Space Complexity: O(N) (storing parents and ranks).
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        for src, dest in edges:
            if not uf.union(src, dest):
                return [src, dest]

        return []
