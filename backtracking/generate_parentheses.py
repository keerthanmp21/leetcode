from typing import List

class Solution:
    # backtracking
    # tc O(2^n), sc O(n)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(openN, closedN, curStr):
            if len(curStr) == n*2:
                res.append(curStr)
                return
            if openN<n:
                backtrack(openN+1, closedN, curStr+'(')
            if closedN<openN:
                backtrack(openN, closedN+1, curStr+')')
        backtrack(0,0,'')
        return res

    # dp
    def generateParenthesis2(self, n: int) -> List[str]:
        dp = [[] for i in range(n + 1)]
        dp[0].append('')

        for i in range(n + 1):
            for j in range(i):
                for x in dp[j]:
                    for y in dp[i - j - 1]:
                        dp[i] += ['(' + x + ')' + y]

        return dp[n]