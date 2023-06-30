# two pointers
# tc O(n), sc O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(1,len(nums)):
            if nums[l] == 0 and nums[r] != 0:
                #swap
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] != 0:
                l += 1

