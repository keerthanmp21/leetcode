class Solution:
    def climbStairs(self, n: int) -> int:
        # backtracking, brute force, recursion
        # tc O(n^2), sc O(n)
        def backtrack(n):
            if n==1:
                return 1
            if n==2:
                return 2
            return backtrack(n-1)+backtrack(n-2)
        return backtrack(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        # dp memoization
        # tc O(n), sc O(n)
        dp = {1:1,2:2}
        def backtrack(n):
            if n in dp:
                return dp[n]
            dp[n] = backtrack(n-1)+backtrack(n-2)
            return dp[n]
        return backtrack(n)
    
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp tabulation
        # time O(n) space O(n)
        if n in [0,1,2]:
            return n
        dp = [0]*(n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]

class Solution:
    def climbStairs(self, n: int) -> int:
        #greedy
        # time O(n) space O(1)
        one, two= 1,1
        
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
            
        return one