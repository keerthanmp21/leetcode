from typing import List


class Solution:
    # brute force
    # tc O(n^2), sc O(1) tle
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        if N == 0:
            return 0
        if N == 1:
            return heights[0]
        maxArea = max(heights)
        for i in range(N):
            minHeight = heights[i]
            for j in range(i + 1, N):
                minHeight = min(minHeight, heights[j])
                maxArea = max(maxArea, minHeight * (j - i + 1))
        return maxArea

    # stack
    # tc O(n), sc O(n)
    def largestRectangleArea2(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            # monotonic increasing stack
            while stack and h < stack[-1][-1]:
                topIndex, topHeight = stack.pop()
                maxArea = max(maxArea, (i - topIndex) * topHeight)
                start = topIndex

            stack.append([start, h])

        N = len(heights)
        for i, h in stack:
            maxArea = max(maxArea, (N - i) * h)

        return maxArea