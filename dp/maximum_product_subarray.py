from typing import List
from functools import cache


class Solution:
    # brute force
    # tc O(n^2), sc O(1)
    def maxProduct1(self, nums: List[int]) -> int:
        N = len(nums)
        res = float("-inf")
        for i in range(N):
            cur = 1
            for j in range(i, N):
                cur *= nums[j]
                res = max(res, cur)
        return res

    # backtrack
    # tc O(2^n), sc O(1)
    def maxProduct2(self, nums: List[int]) -> int:
        N = len(nums)

        def backtrack(idx, value):
            if idx == N:
                return value
            pick = backtrack(idx + 1, value * nums[idx])
            not_pick = backtrack(idx + 1, nums[idx])
            if idx == 0:
                value = nums[0]
            return max(value, pick, not_pick)

        return backtrack(0, 1)

    # dp memoization
    # tc O(n^2), sc O(n)
    def maxProduct3(self, nums: List[int]) -> int:
        N = len(nums)
        dp = {}

        def backtrack(idx, value):
            if idx == N:
                return value
            if (idx, value) in dp:
                return dp[(idx, value)]
            pick = backtrack(idx + 1, value * nums[idx])
            not_pick = backtrack(idx + 1, nums[idx])
            if idx == 0:
                value = nums[0]
            dp[(idx, value)] = max(value, pick, not_pick)
            return dp[(idx, value)]

        return backtrack(0, 1)

    def maxProduct4(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def backtrack(idx, value):
            if idx == N:
                return value
            pick = backtrack(idx + 1, value * nums[idx])
            not_pick = backtrack(idx + 1, nums[idx])
            if idx == 0:
                value = nums[0]
            return max(value, pick, not_pick)

        return backtrack(0, 1)

    # dp tabulation
    # tc O(n), sc O(1)
    def maxProduct5(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
