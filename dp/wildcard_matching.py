# recursion
# tc O(2^n), sc O(n)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lenS = len(s)
        lenP = len(p)
        def recursion(i,j):
            if j == len(p):
                return i == len(s)
            
            # Match Single character
            if i < lenS and (s[i] == p[j] or p[j] == '?'):
                return recursion(i+1, j+1)

            # Match zero or one or more character
            if p[j] == '*':
                return recursion(i, j+1) or i<lenS and recursion(i+1, j)

            return False

        return recursion(0,0)
        

# dp memoization
# tc O(n^2), sc O(n)
class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        lenS = len(s)
        lenP = len(p)
        cache = {}
        def recursion(i,j):
            if j == len(p):
                return i == len(s)
            if (i,j) in cache:
                return cache[(i,j)]
            # Match Single character
            if i < lenS and (s[i] == p[j] or p[j] == '?'):
                cache[(i,j)] = recursion(i+1, j+1)
                return cache[(i,j)]

            # Match zero or one or more character
            if p[j] == '*':
                cache[(i,j)] = recursion(i, j+1) or i<lenS and recursion(i+1, j)
                return cache[(i,j)]

            cache[(i,j)] = False
            return cache[(i,j)]
        return recursion(0,0)
        

class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        # dp tabulation
        # tc O(m*n), sc O(m*n)
        lenS = len(s)
        lenP = len(p)
        dp = [[False]*(lenP+1) for _ in range(lenS+1)]
        dp[0][0] = True
        for i in range(1,lenP+1):
            if p[i-1] != '*':
                break
            dp[0][i] = True

        for i in range(1, lenS+1):
            for j in range(1, lenP+1):
                if p[j-1] in [s[i-1], '?']:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]
            









        