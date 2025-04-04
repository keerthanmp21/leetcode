from typing import List


class Solution:
    # recursion
    # time O(2^n), space O(n)
    def canPartition1(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        def helper(n, total):
            if total == 0:
                return True
            if n == 0 and total != 0:
                return False
            # If last element is greater than sum, then ignore it
            if nums[n - 1] > total:
                return helper(n - 1, total)
            # else, check if sum can be obtained by any of
            # the following
            # (a) including the last element
            # (b) excluding the last element

            return helper(n - 1, total - nums[n - 1]) or helper(n - 1, total)

        return helper(len(nums), total // 2)

    # dp memoization
    # tc O(n^2), sc O(n^2)
    def canPartition2(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        dp = [[-1] * (total + 1) for i in range(len(nums) + 1)]

        def helper(n, total):
            if total == 0:
                return True
            if n == 0 and total != 0:
                return False
            if dp[n][total] != -1:
                return dp[n][total]
            if nums[n - 1] > total:
                return helper(n - 1, total)
            dp[n][total] = helper(n - 1, total - nums[n - 1]) or helper(n - 1, total)
            return dp[n][total]

        return helper(len(nums), total // 2)

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2
        if total % 2 != 0:
            return False
        dp = {}

        def helper(n, total):
            if total == 0:
                return True
            if n == 0 and total != 0:
                return False
            if (n, total) in dp:
                return dp[(n, total)]
            if nums[n - 1] > total:
                dp[(n, total)] = helper(n - 1, total)
                return dp[(n, total)]
            dp[(n, total)] = helper(n - 1, total - nums[n - 1]) or helper(n - 1, total)
            return dp[(n, total)]

        return helper(len(nums), target)
    
    # dp tabulation
    # tc O(n^2), sc O(n^2)
    def canPartition3(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP

        return True if target in dp else False
    
    def canPartition3(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
