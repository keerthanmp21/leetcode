from typing import List

class Solution:
    # recursion
    # tc O(2^n), sc O(n)
    def maxProfit1(self, k: int, prices: List[int]) -> int:
        N = len(prices)

        def backtrack(i, buy, cap):
            if i == N or cap == 0:
                return 0
            profit = 0
            if buy == 0:  # buy the stock
                profit = max(
                    0 + backtrack(i + 1, 0, cap), -prices[i] + backtrack(i + 1, 1, cap)
                )
            else:  # sell the stock
                profit = max(
                    0 + backtrack(i + 1, 1, cap),
                    prices[i] + backtrack(i + 1, 0, cap - 1),
                )
            return profit

        return backtrack(0, 0, k)

        # dp memoization
        # tc O(n^2), sc O(n)

    def maxProfit2(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        dp = {}

        def backtrack(i, buy, cap):
            if i == N or cap == 0:
                return 0
            if (i, buy, cap) in dp:
                return dp[(i, buy, cap)]
            profit = 0
            if buy == 0:  # buy the stock
                profit = max(
                    0 + backtrack(i + 1, 0, cap), -prices[i] + backtrack(i + 1, 1, cap)
                )
            else:  # sell the stock
                profit = max(
                    0 + backtrack(i + 1, 1, cap),
                    prices[i] + backtrack(i + 1, 0, cap - 1),
                )
            dp[(i, buy, cap)] = profit
            return dp[(i, buy, cap)]

        return backtrack(0, 0, k)

        # dp tabulation
        # tc O(Nx2xK), sc O(k)

    def maxProfit3(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        ahead = [[0] * (k + 1) for _ in range(2)]
        cur = [[0] * (k + 1) for _ in range(2)]

        for i in range(N - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, k + 1):
                    if buy == 0:
                        cur[buy][cap] = max(
                            0 + ahead[0][cap], -prices[i] + ahead[1][cap]
                        )
                    if buy == 1:
                        cur[buy][cap] = max(
                            0 + ahead[1][cap], prices[i] + ahead[0][cap - 1]
                        )
            ahead = cur

        return ahead[0][k]
