# backtracking
# time O(2^n), space O(2^n)
class Solution1:
    def rob(self, nums: List[int]) -> int:
        def helper(n):
            if n < 0 :
                return 0
            if n == 0:
                return nums[0]
                
            # if current element is pick then previous cannot be picked
            pick = nums[n] + helper(n-2)
            # if current element is not picked then previous element is picked
            notpick = helper(n-1)
            return max(pick, notpick)

        return helper(len(nums)-1)
        
# dp memoization
# time O(n), space O(n)
class Solution2:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for i in range(len(nums))]
    
        def helper(n):
            if n < 0 :
                return 0
            if n == 0:
                return nums[0]
            if(dp[n] != -1):
                return dp[n]
            pick = nums[n] + helper(n-2)
            notpick = helper(n-1)
            dp[n] = max(pick, notpick)
            return dp[n]
            
        helper(len(nums)-1)
        return max(dp[-1],nums[0])
        
# dp tabulation
# time O(n), space O(n)
class Solution3:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[-1]
    
# greedy
# time O(n), space O(1)
class Solution4:
    def rob(self, nums: List[int]) -> int:
        rob1 , rob2 =0, 0
        
        for n in nums:
            temp = max(n+rob1,rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2