# backtrack
# tc O(3^n) , sc O(n)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def backtrack(i,j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            #if second is * p[i+1]
            if (j+1) < len(p) and p[j+1] == "*":
                # Zero means advance p[j+2]
                # one or more compare and advance if match
                return (backtrack(i,j+2) or (match and backtrack(i+1, j)))
            
            if match:# Match either same or '.'
                return backtrack(i+1, j+1)

            return False # no match
        return backtrack(0,0)
        
# dp memoization
# tc O(n^3), sc O(n)
class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
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
class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        lenS = len(s)
        lenP = len(p)
        dp = [[False]*(lenP+1) for _ in range(lenS+1)]
        dp[0][0] = True

        for i in range(lenP):
            if p[i] == '*' and dp[0][i-1]:
                dp[0][i+1] = True

        for i in range(lenS):
            for j in range(lenP):
                if p[j] == '.' or p[j] == s[i]:
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == '*':
                    if p[j-1] != s[i] and p[j-1] != '.':
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        dp[i+1][j+1] = (dp[i+1][j] or 
                        dp[i][j+1] or dp[i+1][j-1])

        return dp[lenS][lenP]







