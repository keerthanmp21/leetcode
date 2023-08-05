from typing import List

# tc O(logn), sc O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getLeft():
            l, r = 0, len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if target>nums[mid]:
                    l += 1
                else:
                    r -= 1
            return l

        def getRight():
            l, r = 0, len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if target>=nums[mid]:
                    l += 1
                else:
                    r -= 1
            return r

        left ,right = getLeft(), getRight()
        if left<=right:
            return [left, right]
        return [-1,-1]