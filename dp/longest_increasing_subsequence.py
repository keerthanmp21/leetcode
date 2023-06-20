# backtrack
# tc O(2^n), sc O(1)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        def backtrack(i,prev):
            if i == N: return 0
            add, notAdd = 0, 0
            if nums[i] > prev:
                add = 1 + backtrack(i + 1,nums[i])
            notAdd = backtrack(i + 1,prev)
            return max(add, notAdd)
        
        return backtrack(0,float('-inf'))

# dp memoization
# tc O(n^2), sc O(n^2)       
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[-1 for _ in range(N)] for _ in range(N)]   
        def backtrack(i,prev_i):
            if i == N: return 0
            if dp[prev_i + 1][i] != -1:
                return dp[prev_i + 1][i]
            add, notAdd = 0, 0
            if prev_i < 0 or nums[i] > nums[prev_i]:
                add = 1 + backtrack(i+1,i)
            notAdd = backtrack(i + 1,prev_i)
            dp[prev_i + 1][i] = max(add, notAdd)
            return dp[prev_i + 1][i]
        
        return backtrack(0,-1)  

# dp memoization
# tc O(n^2), sc O(n)
class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [-1 for _ in range(N)]
        def backtrack(i, prev_i):
            if i == N:
                return 0
            if dp[prev_i+1] != -1:
                return dp[prev_i+1]
            add = 0
            if prev_i < 0 or nums[i] > nums[prev_i]:
                add = 1 + backtrack(i+1,i)
            notAdd = backtrack(i + 1,prev_i)
            dp[prev_i+1] = max(add, notAdd)
            return dp[prev_i+1]
        return backtrack(0,-1)
        
# dp tabulation
# tc O(n^2), sc O(n)
class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(dp)

# binary search
# tc O(nlogn), sc O(n)
class Solution4:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            l, r = 0, size
            while l != r:
                mid = (l + r) // 2
                if tails[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            tails[l] = x
            size = max(l + 1, size)
        return size
        