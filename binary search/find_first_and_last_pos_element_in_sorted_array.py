from typing import List

# tc O(logn), sc O(1)
class Solution:
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        def getLeft():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def getRight():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if target >= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        left, right = getLeft(), getRight()
        if left <= right:
            return [left, right]
        return [-1, -1]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(target2):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target2:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        lb1 = lower_bound(target)
        lb2 = lower_bound(target + 1) - 1

        if lb1 < len(nums) and nums[lb1] == target:
            return [lb1, lb2]
        else:
            return [-1, -1]
