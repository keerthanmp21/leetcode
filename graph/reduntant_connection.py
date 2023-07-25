from typing import List
from collections import deque, defaultdict

class Solution:
    # union find
    def findRedundantConnection2(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)
        
        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1,n2]

    def findRedundantConnection3(self, edges: List[List[int]]) -> List[int]:
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
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