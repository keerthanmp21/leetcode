from typing import List


class Solution:
    # brute force
    # tc O(n^2), sc O(n)
    def maxArea1(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                res = max(res, area)
        return res

    # two pointers or greedy
    # tc O(n), sc O(n)
    def maxArea2(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
