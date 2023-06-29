# sorting
# tc O(nlogn), sc O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

# count sort 
# tc O(n), sc O(3)

class Solution2:
    def sortColors(self, nums: List[int]) -> None:      
        no_of_occ = [0,0,0]
        for i in nums:
            no_of_occ[i] += 1
        i = 0
        for key, value in enumerate(no_of_occ):
            for j in range(value):
                nums[i] = key
                i += 1

# two pointers
# tc O(n), sc O(1)
class Solution3:
    def sortColors(self, nums: List[int]) -> None: 
        i, l, r = 0, 0, len(nums)-1 #l->0,i->1, r->2
        while i<=r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
        