from typing import List
import collections

class Solution:
    #dfs
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = collections.defaultdict(dict)
        for (pt1,pt2), value in zip(equations,values):
            edges[pt1][pt2] = value
            edges[pt2][pt1] = 1/value
        visit = set()
        result = []

        def dfs(cur, dest, totalVal):
            if cur == dest:
                return totalVal
            for key, value in edges[cur].items():
                if key not in visit:
                    visit.add(key)
                    result = dfs(key, dest,value*totalVal)
                    if result != -1:
                        return result
                    visit.remove(key)
            return -1


        for src, dest in queries:
            result.append(dfs(src,dest,1) if src in edges else -1)
            visit = set()
        return result

    # bfs
    def calcEquation2(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = collections.defaultdict(dict)
        for (pt1,pt2), value in zip(equations,values):
            edges[pt1][pt2] = value
            edges[pt2][pt1] = 1/value
        result = []
        for src, dest in queries:
            q = collections.deque()
            visit = set()
            totalVal = -1
            if src in edges:
                q.append((src,1))
                visit.add(src)
            while q:
                cur, value = q.popleft()
                if cur == dest:
                    totalVal = value
                    break
                for edge_key, edg_value in edges[cur].items():
                    if edge_key not in visit:
                        visit.add(edge_key)
                        q.append((edge_key,edg_value*value))
            result.append(totalVal)
        return result
