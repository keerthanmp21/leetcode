from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for start, end, height in buildings:
            points.append([start,end,-height]) #-ve = max heap
            points.append([end,0,0]) #if there is no overlap buidling then end will be 0 and height 0

        points.sort(key=lambda x:(x[0],x[2],x[1]))

        output = [[0,0]]
        heap = [[0,float('infinity')]]
        for start, end, height in points:
            while heap and heap[0][1] <= start:
                heapq.heappop(heap)
            if height != 0:
                heapq.heappush(heap,[height,end])
            if output[-1][1] != -heap[0][0]:
                output.append([start,-heap[0][0]])

        return output[1:]