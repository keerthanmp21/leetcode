from typing import List


class Solution:
    # backtracking or memoization
    # tc O(2^n), sc O(n)
    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        n = len(cost)

        def helper(i):
            if i <= 1:
                return cost[i]
            return min(helper(i - 1) + cost[i], helper(i - 2) + cost[i])

        return min(helper(n - 1), helper(n - 2))

    # dp memoization
    # time O(n), space O(n)
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n

        def helper(i):
            if i <= 1:
                return cost[i]
            if dp[i] != -1:
                return dp[i]
            dp[i] = min(helper(i - 1) + cost[i], helper(i - 2) + cost[i])
            return dp[i]

        return min(helper(n - 1), helper(n - 2))

    # dp tabulation in memory
    # time O(n), space O(1)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])
