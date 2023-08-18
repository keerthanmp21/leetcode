from typing import List
from collections import deque


class Solution:
    # dfs
    # tc O(n+p) n = nunCourses, p = prerequisites
    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()  # all courses along the curr dfs path

        def dfs(crs):
            if crs in visitSet:  # cycle
                return False
            if preMap[crs] == []:  # can be completed if no prereq
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)  # we have already finished visiting it
            preMap[crs] = []  # can be visited again avoid repeating its neighbor
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True

    # bfs
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = [[] for i in range(numCourses)]
        degrees = [0] * numCourses

        for crs, preCrs in prerequisites:
            preMap[preCrs].append(crs)
            # preCrs as key coz bfs starts from course which has no outgoing edge
            degrees[crs] += 1

        q = deque(cur for cur, degree in enumerate(degrees) if not degree)

        while q:
            cur = q.popleft()
            for nextCourse in preMap[cur]:
                degrees[nextCourse] -= 1
                if not degrees[nextCourse]:
                    q.append(nextCourse)

        return not sum(degrees)


# s = Solution()
# print(s.canFinish(5,[[0,1],[0,2],[1,3],[1,4],[3,4]]))
# print(s.canFinish(3,[[0,1],[1,2],[2,0]])) # loop matches base cond line no. 13
