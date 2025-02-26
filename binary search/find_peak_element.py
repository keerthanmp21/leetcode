from typing import List

# tc O(logn), sc O(1)
class Solution:
    def findPeakElement1(self, nums: List[int]) -> int:
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

    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:  # Peak must be on the right
                l = mid + 1
            else:  # Peak is on the left or mid is the peak
                r = mid
        return l  # or return r (both point to the peak)


                
        