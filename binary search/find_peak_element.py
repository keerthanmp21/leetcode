from typing import List

# tc O(logn), sc O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
        return l

                
        