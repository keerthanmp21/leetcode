from typing import List
from collections import deque

class Solution:
    # dfs
    def canVisitAllRooms2(self, rooms: List[List[int]]) -> bool:
        visitSet = set()

        def dfs(key):
            if key in visitSet:
                return
            visitSet.add(key)
            for neiKey in rooms[key]:
                dfs(neiKey)

        dfs(0)
        return len(visitSet) == len(rooms)

    # bfs
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visitSet = set([0])

        while q:
            key = q.popleft()
            for neiKey in rooms[key]:
                if neiKey not in visitSet:
                    q.append(neiKey)
                    visitSet.add(neiKey)

        return len(visitSet) == len(rooms)
