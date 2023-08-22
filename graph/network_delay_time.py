from typing import List
import collections
import heapq
from collections import defaultdict, deque


class Solution:
    # dijstra (shortest path) => bfs (using min heap)
    # tc O(Elogv)
    def networkDelayTime1(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append([v, w])

        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return t if len(visit) == n else -1

    # bellman-ford
    # tc O(EV)
    def networkDelayTime2(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[k - 1] = 0

        for _ in range(n - 1):
            for u, v, w in times:
                if dist[u - 1] + w < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + w

        return max(dist) if max(dist) < float("inf") else -1

    # spfa (shortest path fastest algorithm)
    # tc O(E), sc O(V+E)
    def networkDelayTime3(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[k - 1] = 0
        edges = defaultdict(dict)
        for u, v, w in times:
            edges[u][v] = w
        q = deque([k])
        while q:
            u = q.popleft()
            for v, w in edges[u].items():
                if dist[u - 1] + w < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + w
                    q.append(v)

        return max(dist) if max(dist) < float("inf") else -1

    # floyd-warshall
    # tc O(v^3), sc O(v^2)
    def networkDelayTime4(self, times: List[List[int]], n: int, k: int) -> int:
        cost = {}
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    cost[(i, j)] = 0
                else:
                    cost[(i, j)] = float("inf")

        for u, v, c in times:
            cost[(u, v)] = c

        for mid in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    cost[(i, j)] = min(cost[(i, j)], cost[(i, mid)] + cost[(mid, j)])

        res = float("-inf")
        for i in range(1, n + 1):
            res = max(res, cost[(k, i)])

        return res if res != float("inf") else -1

    # dfs
    # tc O(2n+V), sc O(2n)
    def networkDelayTime5(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append([v, w])
        dist = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node, totalTime):
            if totalTime >= dist[node]:  # already visited
                return
            dist[node] = totalTime
            for nei, time in sorted(edges[node]):
                dfs(nei, time + totalTime)

        dfs(k, 0)
        res = max(dist.values())
        return res if res < float("inf") else -1
