from typing import List


# two pointers and sorting
# tc O(nlogn), sc O(1)
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        total_count = 0
        while l < r:
            _sum = nums[l] + nums[r]
            if _sum < k:
                l += 1
            elif _sum > k:
                r -= 1
            else:
                total_count += 1
                l += 1
                r -= 1
        return total_count
