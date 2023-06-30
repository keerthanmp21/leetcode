# brute force
# tc O(kn), sc O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            last_ele = nums[-1]
            nums[1:] = nums[0:-1]
            nums[0] = last_ele

# two pointers
# tc O(n), sc O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        N = len(nums)
        def rotateNums(l,r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            
        if k>N:
            k = k%N
        
        if k>0:
            rotateNums(0,N-1)
            rotateNums(0,k-1)
            rotateNums(k,N-1)