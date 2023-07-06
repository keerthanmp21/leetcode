class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][-1]:
                topInd, topvalue = stack.pop()
                res[topInd] = (i-topInd)
            stack.append([i,t])

        return res