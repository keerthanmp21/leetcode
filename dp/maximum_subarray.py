# brute force
# tc O(n^2), sc O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                res = max(res, cur_sum)

        return res

# dp recursive
# tc O(n^2), sc O(n)
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        def solve(i, must_pick):
            if i >= len(nums): return 0 if must_pick else -inf
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)

# dp memoization
# tc O(n), sc O(n)
class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        @cache
        def solve(i, must_pick):
            if i >= len(nums): return 0 if must_pick else -inf
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)
        
# dp tabulation
# tc O(n), sc O(n)
class Solution4:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [[0]*len(nums) for i in range(2)]
        dp[0][0], dp[1][0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[1][i] = max(nums[i], nums[i] + dp[1][i-1])
            dp[0][i] = max(dp[0][i-1], dp[1][i])
        return dp[0][-1]
        
class Solution5:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)
        
# greedy
# time O(n), sc O(1)
class Solution6:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res

