# stack
# tc O(n), sc O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    res = max(res,i-stack[-1])
        return res
        
#dp tabulation
# tc O(n), sc O(n)
class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)
        dp = [0]*N
        res = 0
        leftCount = 0
        for i in range(N):
            if s[i] == '(':
                leftCount += 1
            elif leftCount>0:
                dp[i] = dp[i-1]+2
                if (i-dp[i]) >= 0:
                    dp[i] += dp[i-dp[i]]
                res = max(res, dp[i])
                leftCount -= 1
        return res    



