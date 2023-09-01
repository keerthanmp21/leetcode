from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        charSet = set()
        l = 0
        res = 0
        subArraySum = 0

        for r in range(len(nums)):
            while nums[r] in charSet:
                charSet.remove(nums[l])
                subArraySum -= nums[l]
                l += 1
            charSet.add(nums[r])
            subArraySum += nums[r]
            res = max(res, subArraySum)
        return res
