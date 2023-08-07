from typing import List
from functools import cache

class Solution:
    # recursion
    # tc O(2^n), sc O(n)
    def maxProfit1(self, prices: List[int]) -> int:
        N = len(prices)

        def recursion(day, transactionLeft):
            if day == N:
                return 0
            if transactionLeft == 0:
                return 0

            # no transaction today
            res1 = recursion(day + 1, transactionLeft)

            # doing the possible transaction today
            res2 = 0
            buy = transactionLeft % 2

            if buy == 0:  # buy
                res2 = -prices[day] + recursion(day + 1, transactionLeft - 1)
            else:  # sell
                res2 = prices[day] + recursion(day + 1, transactionLeft - 1)

            return max(res1, res2)

        return recursion(0, 4)

    # dp memoization
    # tc O(n), sc O(n)
    def maxProfit2(self, prices: List[int]) -> int:
        N = len(prices)
        dp = {}

        def recursion(day, transactionLeft):
            if day == N:
                return 0
            if transactionLeft == 0:
                return 0
            if (day, transactionLeft) in dp:
                return dp[(day, transactionLeft)]
            # no transaction today
            res1 = recursion(day + 1, transactionLeft)

            # doing the possible transaction today
            res2 = 0
            buy = transactionLeft % 2

            if buy == 0:  # buy
                res2 = -prices[day] + recursion(day + 1, transactionLeft - 1)
            else:  # sell
                res2 = prices[day] + recursion(day + 1, transactionLeft - 1)
            dp[(day, transactionLeft)] = max(res1, res2)
            return dp[(day, transactionLeft)]

        return recursion(0, 4)

    def maxProfit3(self, prices: List[int]) -> int:
        N = len(prices)

        @cache
        def recursion(day, transactionLeft):
            if day == N:
                return 0
            if transactionLeft == 0:
                return 0
            # no transaction today
            res1 = recursion(day + 1, transactionLeft)

            res2 = 0
            buy = transactionLeft % 2

            if buy == 0:
                res2 = -prices[day] + recursion(day + 1, transactionLeft - 1)
            else:
                res2 = prices[day] + recursion(day + 1, transactionLeft - 1)
            return max(res1, res2)

        return recursion(0, 4)

    def maxProfit4(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0] * 5 for _ in range(N + 1)]

        for day in range(N - 1, -1, -1):
            for transactionLeft in range(5):
                res = dp[day][transactionLeft]
                if day == N:
                    res = 0
                elif transactionLeft == 0:
                    res = 0
                else:
                    # no transaction today
                    res1 = dp[day + 1][transactionLeft]

                    res2 = 0
                    # transaction today
                    buy = transactionLeft % 2
                    if buy == 0:
                        # buy
                        res2 = -prices[day] + dp[day + 1][transactionLeft - 1]
                    else:
                        # sell
                        res2 = prices[day] + dp[day + 1][transactionLeft - 1]
                    res = max(res1, res2)
                dp[day][transactionLeft] = res
        return dp[0][4]
