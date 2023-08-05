from typing import List

# tc O(logn), sc O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]: # left side rotated
                if nums[l] <= target < nums[mid]:
                    # if it is left rotated then obviously
                    # nums[l] will be lesser then nums[mid]
                    # so here we can compare l<=target<mid
                    r = mid-1
                else:
                    l = mid+1
            else: # right side rotated
                if nums[mid] < target <= nums[r]:
                    # if it is left rotated then obviously
                    # nums[l] will be greater then nums[mid]
                    # here we cant compare l<=target<mid
                    # thats why compare mid<target<=r
                    l = mid+1
                else:
                    r = mid-1
                

        return -1