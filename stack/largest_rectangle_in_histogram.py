class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            # monotonic increasing stack
            while stack and h < stack[-1][-1]:
                index, height = stack.pop()
                maxArea = max(maxArea, (i-index)*height)
                start = index
            stack.append([start, h])

        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))

        return maxArea