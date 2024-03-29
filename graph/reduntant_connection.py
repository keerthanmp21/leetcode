from typing import List
from collections import deque, defaultdict

class Solution:
    # union find
    # time O(n), space O(n)
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
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