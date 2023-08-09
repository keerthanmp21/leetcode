from typing import List


class Solution:
    # backtrack recursion
    # tc O(n^n), sc O(1)
    def numSquares1(self, n: int) -> int:
        def backtrack(num):
            if num < 4:
                return num
            res = num
            for i in range(1, num + 1):
                square = i * i
                if square <= num:
                    res = min(res, 1 + backtrack(num - square))
            return res

        return backtrack(n)

    # dp memoization
    # tc O(n^2), sc O(n)
    def numSquares2(self, n: int) -> int:
        cache = {}

        def backtrack(num):
            if num < 4:
                return num
            if num in cache:
                return cache[num]
            res = num
            for i in range(1, num + 1):
                square = i * i
                if square <= num:
                    res = min(res, 1 + backtrack(num - square))
            cache[num] = res
            return cache[num]

        return backtrack(n)

    # dp tabulation
    # tc O(n^2), sc O(n)
    def numSquares3(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]
