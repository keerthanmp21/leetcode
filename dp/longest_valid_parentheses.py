class Solution:
    # stack
    # tc O(n), sc O(n)
    def longestValidParentheses2(self, s: str) -> int:
        '''
        we only update the result(max) when we find a "pair".
        If we find a pair. We throw this pair away and see how big the gap is 
        between current and previous invalid.
        '''
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == ')' and len(stack) > 1 and s[stack[-1]] == '(':
                stack.pop()
                res = max(res, i-stack[-1])
            else:
                stack.append(i)
        return res
        
        
    # dp tabulation
    # tc O(n), sc O(n)
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)
        dp = [0]*N
        res = 0
        leftCount = 0
        for i in range(N):
            if s[i] == '(':
                leftCount += 1
            elif leftCount > 0:
                leftCount -= 1
                dp[i] = dp[i-1]+2
                if (i-dp[i]) >= 0:
                    dp[i] += dp[i-dp[i]]
                res = max(res, dp[i])
                
        print(dp)
        return res    

s = Solution()
print(s.longestValidParentheses('()(())'))
