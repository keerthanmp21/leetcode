from typing import List


# sliding window
# tc O(n), sc O(1)
class Solution:
    def findMaxAverage1(self, nums: List[int], k: int) -> float:
        l = 0
        res = float("-inf")
        total = 0
        for r in range(len(nums)):
            if r < k:
                total += nums[r]
            else:
                res = max(res, total)
                total += nums[r] - nums[l]
                l += 1
        res = max(res, total)
        return res / k

    def findMaxAverage2(self, nums: List[int], k: int) -> float:
        l = 0
        total = sum(nums[:k])
        res = total
        for r in range(k, len(nums)):
            res = max(res, total)
            total += nums[r] - nums[l]
            l += 1
        res = max(res, total)
        return res / k
