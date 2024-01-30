from typing import List
import collections
import heapq
from collections import *

class Solution:
    # bellman-ford
    # tc O(V^3)
    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        
        for i in range(k+1):
            temPrices = prices.copy()
            for s,d,p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s]+p < temPrices[d]:
                    temPrices[d] = prices[s]+p
            prices = temPrices
            
        return -1 if prices[dst] == float('inf') else prices[dst]
        

    # dijkstra 
    # tc O(V^2)
    def findCheapestPrice3(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for frm, to, price in flights:
            graph[frm][to] = price
        minHeap = [(0, src, k+1)]
        visit = [0] * n # we can use hashset
        while minHeap:
            price, curNode, k = heapq.heappop(minHeap)
            if curNode == dst:
                return price
            if visit[curNode] >= k:
                continue
            visit[curNode] = k
            for neiNode, neiPrice in graph[curNode].items():
                heapq.heappush(minHeap, (price+neiPrice, neiNode, k-1))
        return -1

    # spfa
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = defaultdict(list)
        for u,v,w in flights:
            edges[u].append([v,w])
        cost = {src:0}
        q = deque([(src,0,0)])

        while q:
            cur, price, k_taken = q.popleft()
            for neiCity, neiPrice in edges[cur]:
                if neiCity not in cost or neiPrice + price < cost[neiCity]:
                    cost[neiCity] = neiPrice + price
                    if k_taken < k:
                        q.append((neiCity, cost[neiCity],k_taken+1))

        return cost.get(dst, -1)