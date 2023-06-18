class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #backtrack
        # tc = O(n^n), sc = O(n)
        
        N = len(nums)
        def backtrack(ind):
            if ind == N-1:
                return True
            if nums[ind] == 0:
                return False
            max_jump = ind+nums[ind]
            for jump in range(ind+1, max_jump+1):
                if jump < N and backtrack(jump):
                    return True
            return False
        return backtrack(0)
        
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp top down
        # tc = O(n*n), sc = O(n)+O(n) stack with dp
        N = len(nums)
        dp = [-1]*N
        def backtrack(ind):
            if ind == N-1:
                return True
            if nums[ind] == 0:
                return False
            if dp[ind] != -1:
                return dp[ind]
            max_jump = ind+nums[ind]
            for jump in range(ind+1, max_jump+1):
                if jump < N and backtrack(jump):
                    dp[ind] = True
                    return dp[ind]
            dp[ind] = False
            return dp[ind]
        return backtrack(0)
        
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @lru_cache(None)
        def dp(i):
            if i == n - 1:
                return True
            
            for j in range(i+1, min(i+nums[i], n-1) + 1):
                if dp(j):
                    return True
            return False
        
        return dp(0)
    
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp tabulation
        # tc O(n^2), sc O(n)
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            #min(n, i+nums[i]+1) if we cant reach to next pos
            # then inner for loop will not execute and dp of 
            # that pos will remains False always so all pos
            # prev to that will remain False
            for j in range(i+1, min(n, i+nums[i]+1)):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy
        # O(n)
        
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i+nums[i] >= goal:
                goal = i

        if goal == 0:
            return True
        else:
            return False
        