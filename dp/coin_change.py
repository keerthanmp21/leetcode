from typing import List


class Solution:
    # backtracking recursion
    # tc O(2^n), sc O(n)
    def coinChange1(self, coins: List[int], amount: int) -> int:
        N = len(coins)

        def backtrack(idx, amount):
            if amount == 0:
                return 0
            if idx == -1:
                return float("inf")
            res = backtrack(idx - 1, amount)  # skip coin
            if amount >= coins[idx]:  # use coin
                res = min(res, backtrack(idx, amount - coins[idx]) + 1)
            return res

        res = backtrack(N - 1, amount)
        return res if res != float("inf") else -1

    # dp memoization
    # tc O(n*amount), sc O(n*amount)
    def coinChange2(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        dp = {}

        def backtrack(idx, amount):
            if amount == 0:
                return 0
            if idx == -1:
                return float("inf")
            if (idx, amount) in dp:
                return dp[(idx, amount)]
            res = backtrack(idx - 1, amount)  # skip coin
            if amount >= coins[idx]:  # use coin
                res = min(res, backtrack(idx, amount - coins[idx]) + 1)
            dp[(idx, amount)] = res
            return res

        res = backtrack(N - 1, amount)
        return res if res != float("inf") else -1

    # dp tabulation
    # tc O(n*amount), sc O(amount)
    def coinChange3(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    # min(skip coin, use coin)

        return dp[amount] if dp[amount] != amount + 1 else -1
