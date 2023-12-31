from typing import List


class Solution:
    # greedy
    # tc O(n), sc O(1)
    def missingNumber1(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res

    # binary search
    # tc O(nlogn), sc O(1)
    def missingNumber2(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # number is missing b/w mid and r
            if nums[mid] == mid:
                l = mid + 1
            else:
                r = mid - 1
        return l
