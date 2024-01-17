from typing import List
from math import inf
from functools import cache


class Solution:
    # brute force
    # tc O(n^2), sc O(1)
    def maxSubArray1(self, nums: List[int]) -> int:
        res = float("-inf")
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                res = max(res, cur_sum)

        return res

    # dp recursive
    # tc O(n^2), sc O(n)
    def maxSubArray2(self, nums: List[int]) -> int:
        def solve(i, must_pick):
            if i >= len(nums):
                if must_pick:
                    return 0
                else:
                    return -inf
            if must_pick:
                # either stop here or choose current element and recurse
                return max(nums[i] + solve(i + 1, True), 0)
            else:
                # try both choosing current element or not choosing
                return max(nums[i] + solve(i + 1, True), solve(i + 1, False))

        return solve(0, False)

    # dp memoization
    # tc O(n), sc O(n)
    def maxSubArray3(self, nums: List[int]) -> int:
        @cache
        def solve(i, must_pick):
            if i >= len(nums):
                return 0 if must_pick else -inf
            return max(
                nums[i] + solve(i + 1, True), 0 if must_pick else solve(i + 1, False)
            )

        return solve(0, False)

    # dp tabulation
    # tc O(n), sc O(n)
    def maxSubArray4(self, nums: List[int]) -> int:
        dp = [[0] * len(nums) for _ in range(2)]
        dp[0][0], dp[1][0] = nums[0], nums[0]
        '''
        At each index, we update dp[1][i] as max between either only choosing current element = nums[i] or extending from previous subarray and choosing current element as well = dp[1][i-1] + nums[i]
Similarly, dp[0][1] can be updated as max between maximum sum subarray found till last index = dp[0][i-1] or max subarray sum found ending at current index dp[1][i]
'''
        for i in range(1, len(nums)):
            # maximum subarray sum ending at i (including nums[i])
            dp[1][i] = max(nums[i], nums[i] + dp[1][i - 1])
            # maximum subarray sum upto i (may or may not include nums[i]).
            dp[0][i] = max(dp[0][i - 1], dp[1][i])
        return dp[0][-1]

    # optimized above approach
    def maxSubArray5(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N
        res = dp[0] = nums[0]

        for i in range(1,N):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
            res = max(res, dp[i])

        return res

    def maxSubArray6(self, nums: List[int]) -> int:
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)

    # greedy
    # time O(n), sc O(1)
    def maxSubArray7(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res

    # kadane's algor
    # tc O(n), sc O(n)
    def maxSubArray7(self, nums: List[int]) -> int:
        cur_max, max_till_now = 0, -inf
        for n in nums:
            cur_max = max(cur_max, cur_max + n)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now
    
# recursive
"""
                                                f(0, False)                       🔽 => repeated calculations
					                          /             \ 
                       		       f(1, False)              f(1, True)
			                      /          \       🔽          \      🔽
			                 f(2, False)      f(2, True)           f(2, True)
							/            \  🔽       \   🔽           \  🔽
						f(3, False)   f(3,True)     f(3, True)           f(3, True)
						/        \            \           \                  \
				      ...        ...          ...         ...                ...
"""
