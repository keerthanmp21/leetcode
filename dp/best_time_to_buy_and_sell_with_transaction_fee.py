from typing import List
from functools import lru_cache

class Solution:
    # recursion
    # tc O(2^n), sc O(n)
    def maxProfit1(self, prices: List[int], fee: int) -> int:
        N = len(prices)

        def backtrack(i, buy):
            if i == N:
                return 0

            res = backtrack(i + 1, buy)  # Skip
            if buy:
                res = max(res, backtrack(i + 1, False) - prices[i])
            else:
                res = max(res, backtrack(i + 1, True) + prices[i] - fee)
            return res

        return backtrack(0, True)

        # dp memoization
        # tc O(n*2*2), sc O(n)

    def maxProfit2(self, prices: List[int], fee: int) -> int:
        N = len(prices)

        @lru_cache(None)
        def backtrack(i, buy):
            if i == N:
                return 0

            res = backtrack(i + 1, buy)  # Skip
            if buy:
                res = max(res, backtrack(i + 1, False) - prices[i])
            else:
                res = max(res, backtrack(i + 1, True) + prices[i] - fee)
            return res

        return backtrack(0, True)

        # dp tabulation
        # tc O(n*2*2), sc O(n*2)

    def maxProfit3(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(2):
                if j == 1:
                    dp[i][j] = max(dp[i + 1][j], dp[i + 1][0] - prices[i])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i + 1][1] + prices[i] - fee)

        return dp[0][1]

        # dp tabulation
        # tc O(n*2*2), sc O(1)

    def maxProfit4(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp, dpPrev = [0, 0], [0, 0]

        for i in range(n - 1, -1, -1):
            for j in range(2):
                if j == 1:
                    dp[j] = max(dpPrev[j], dpPrev[0] - prices[i])
                else:
                    dp[j] = max(dpPrev[j], dpPrev[1] + prices[i] - fee)
            dpPrev = dp

        return dpPrev[1]
