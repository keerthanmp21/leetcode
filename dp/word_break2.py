from typing import List


class Solution:
    # backtracking
    # tc O(len(wordDict)^len(s)), sc O(n)
    def wordBreak1(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)

        def backtrack(start):
            res = []
            if start == N:
                res.append("")
                return res

            curStr = s[start:]
            for word in wordDict:
                if curStr.startswith(word):
                    subList = backtrack(start + len(word))
                    for l in subList:
                        if l:
                            res.append(word + " " + l)
                        else:
                            res.append(word + l)

            return res

        return backtrack(0)

    # dp memoization
    # tc O(len(wordDict)^len(s/min word in dict)), sc O(n)
    def wordBreak2(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        cache = [-1] * (N + 1)

        def backtrack(start):
            if cache[start] != -1:
                return cache[start]

            res = []
            if start == N:
                res.append("")
                return res

            curStr = s[start:]
            for word in wordDict:
                if curStr.startswith(word):
                    subList = backtrack(start + len(word))
                    for l in subList:
                        if l:
                            res.append(word + " " + l)
                        else:
                            res.append(word + l)
            cache[start] = res
            return cache[start]

        return backtrack(0)

    # dp tabulation
    # tc O(n^2*len(s)), sc O(n^2)
    def wordBreak3(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        n = len(s)
        dp_solution = [[] for _ in range(n)] + [[""]]
        dp = [0] * n + [1]

        for k in range(n):
            for j in range(k, -1, -1):
                if s[j : k + 1] in wordSet:
                    dp[k] = max(dp[k], dp[j - 1])

        if dp[-2] == 0:
            return []

        for k in range(n):
            for j in range(k, -1, -1):
                if s[j : k + 1] in wordSet:
                    for sol in dp_solution[j - 1]:
                        dp_solution[k].append(sol + " " + s[j : k + 1])

        return [s[1:] for s in dp_solution[-2]]
