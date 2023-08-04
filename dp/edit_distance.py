class Solution:
    #backtrack
    # tc O(3^n), sc O(n)
    def minDistance1(self, word1: str, word2: str) -> int:
        M = len(word1)
        N = len(word2)
        def backtrack(i,j):
            if i == M and j == N:
                return 0
            if i == M:
                return N-j
            if j == N:
                return M-i
            if word1[i] == word2[j]:
                res = backtrack(i+1, j+1)
            else:
                insert = 1+backtrack(i, j+1)
                delete = 1+backtrack(i+1, j)
                replace = 1+backtrack(i+1, j+1)
                res = min(insert, delete, replace)
            return res
        return backtrack(0, 0)
    
    # dp memoization
    # tc O(n^3), sc O(1) 
    def minDistance2(self, word1: str, word2: str) -> int:
        
        M = len(word1)
        N = len(word2)
        cache = {}
        def dfs(i, j):
            if i == M and j == N:
                return 0
            if i == M:
                return N-j
            if j == N:
                return M-i
            if (i,j) not in cache:
                if word1[i] == word2[j]:
                    res = dfs(i+1, j+1)
                else:
                    insert = 1+dfs(i, j+1)
                    delete = 1+dfs(i+1, j)
                    replace = 1+dfs(i+1, j+1)
                    res = min(insert, delete, replace)
                cache[(i,j)] = res
            return cache[(i,j)]

        return dfs(0, 0)

    # dp tabulation
    # tc O(m*n), sc O(m*n)
    def minDistance3(self, word1: str, word2: str) -> int:
        M = len(word1)
        N = len(word2)
        dp = [[0]*(N+1) for _ in range(M+1)]
        for i in range(M+1):
            dp[i][0] = i
        for i in range(N+1):
            dp[0][i] = i
        for i in range(1,M+1):
            for j in range(1,N+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return dp[-1][-1]


