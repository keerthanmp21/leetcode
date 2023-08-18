from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            # monotonic decreasing
            while stack and t > stack[-1][-1]:
                topInd, _ = stack.pop()
                res[topInd] = i - topInd
            stack.append([i, t])

        return res
