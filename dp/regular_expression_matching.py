class Solution:
    # backtrack
    # tc O(3^n) , sc O(n)
    def isMatch3(self, s: str, p: str) -> bool:
        def backtrack(i,j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            '''
            if j >= len(p):
                return i == len(s)
            '''
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j+1) < len(p) and p[j+1] == "*":
                '''
                if (j+1) == '*' then
                1) for zero match = backtrack(i,j+2), j moves i stays at same pos
                2) for more matches = backtrack(i+1, j) inc only i, j stays same
                in 2) we are considering match coz we need to inc i if s[i] and p[i] does not match we should inc i
                '''
                return (backtrack(i,j+2) or (match and backtrack(i+1, j)))
            
            if match:# Match either same or '.'
                return backtrack(i+1, j+1)

            return False # no match
        return backtrack(0,0)
        
    # dp memoization
    # tc O(n^3), sc O(n)
    def isMatch2(self, s: str, p: str) -> bool:
        cache = {}
        
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j+1) < len(p) and p[j+1] == "*":
                cache[(i,j)] = (dfs(i,j+2) or (match and dfs(i+1, j)))
                return cache[(i,j)]
            
            if match:
                cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)]
            cache[(i,j)] = False
            return False
        return dfs(0,0)
        
    # dp tabulation
    # tc O(m*n), sc O(m*n)
    def isMatch(self, s: str, p: str) -> bool:
        lenS = len(s)
        lenP = len(p)
        dp = [[False]*(lenP+1) for _ in range(lenS+1)]
        dp[lenS][lenP] = True

        for i in range(lenS,-1,-1):
            for j in range(lenP-1,-1,-1):
                match = (i<lenS) and (s[i] == p[j] or p[j] == '.')
                if((j+1)<lenP and p[j+1] == '*'):
                    dp[i][j] = dp[i][j+2] or (match and dp[i+1][j])
                else:
                    dp[i][j] = match and dp[i+1][j+1]

        return dp[0][0]