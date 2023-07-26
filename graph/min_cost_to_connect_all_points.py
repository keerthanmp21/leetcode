from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ptLen = len(points)
        adj_dict = defaultdict(list)
        for i in range(ptLen):
            x1, y1 = points[i]
            for j in range(i+1, ptLen):
                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                adj_dict[i].append([cost, j])
                adj_dict[j].append([cost,i])

        minHeap = [[0,0]]
        visited = set()
        res = 0

        while len(visited)<ptLen:
            cost, node1 = heapq.heappop(minHeap)
            if node1 in visited:
                continue
            res += cost
            visited.add(node1)
            for neiCost, nei in adj_dict[node1]:
                if nei not in visited:
                    heapq.heappush(minHeap,[neiCost, nei])
        
        return res