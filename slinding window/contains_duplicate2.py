from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        d = {nums[0]: 1}
        l = 0
        for r in range(1, len(nums)):
            if nums[r] in d:
                return True
            if abs(l - r) > k - 1:
                d[nums[l]] = d[nums[l]] - 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                l += 1
            d[nums[r]] = d.get(nums[r], 0) + 1
        return False
