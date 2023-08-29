from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        total = 1
        res = 0

        for r in range(len(nums)):
            total = total * nums[r]
            while l < len(nums) and total >= k:
                total = total / nums[l]
                l += 1
            if total < k:
                res += r - l + 1

        return max(res, 0)
