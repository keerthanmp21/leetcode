from typing import List
from collections import defaultdict, deque


class Solution:
    # dfs
    def calcEquation1(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = defaultdict(dict)
        for (pt1, pt2), val in zip(equations, values):
            edges[pt1][pt2] = val
            edges[pt2][pt1] = 1/val

        visited = set()
        result = []

        def dfs(cur, dest, totalVal):
            if cur == dest:
                return totalVal
            for nei, val in edges[cur].items():
                if nei not in visited:
                    visited.add(nei)
                    res = dfs(nei, dest, totalVal * val)
                    if res != -1:
                        return res
                    visited.remove(nei)
            return -1

        for src, dest in queries:
            result.append(dfs(src, dest, 1) if src in edges else -1)
            visited = set()

        return result

    # bfs
    def calcEquation2(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = {}
        for (pt1, pt2), val in zip(equations, values):
            if pt1 not in edges:
                edges[pt1] = {pt2 : val}
            else:
                edges[pt1][pt2] = val
            if pt2 not in edges:
                edges[pt2] = {pt1 : 1/val}
            else:
                edges[pt2][pt1] = 1/val
        result = []

        for src, dest in queries:
            q = deque()
            visitSet = set()
            totalVal = -1
            if src in edges:
                q.append((src, 1))
                visitSet.add(src)
            while q:
                cur, val = q.popleft()
                if cur == dest:
                    totalVal = val
                    break
                for nei, neiVal in edges[cur].items():
                    if nei not in visitSet:
                        visitSet.add(nei)
                        q.append((nei, val * neiVal))
            result.append(totalVal)

        return result
