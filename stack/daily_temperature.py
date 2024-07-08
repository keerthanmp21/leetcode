from typing import List


class Solution:
    # brute force (tle)
    # time O(n^2), space O(n)
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [0] * N

        for i in range(N):
            t1 = temperatures[i]
            for j in range(i + 1, N):
                t2 = temperatures[j]
                if t2 > t1:
                    res[i] = (j - i)
                    break

        return res
    
    # monotonic decreasing stack
    # time O(n), space O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [0] * N
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                topInd, topTemp = stack.pop()
                res[topInd] = (i - topInd)
            stack.append([i, t])

        return res
