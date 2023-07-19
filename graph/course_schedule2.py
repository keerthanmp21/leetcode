from typing import List
from collections import deque

class Solution:
    # dfs
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
            
        output = []
        visit, cycle = set(), set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
            
        return output
    
    # bfs
    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = [[] for i in range(numCourses)]
        degrees = [0]*numCourses
        output = []
        q = deque()

        for cur, preCur in prerequisites:
            edges[preCur].append(cur)
            degrees[cur] += 1

        for cur, degree in enumerate(degrees):
            if degree == 0:
                q.append(cur)

        while q:
            cur = q.popleft()
            output.append(cur)
            for preCur in edges[cur]:
                degrees[preCur] -= 1
                if degrees[preCur] == 0:
                    q.append(preCur)
        
        return output if len(output) == numCourses else []