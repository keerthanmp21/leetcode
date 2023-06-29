# brute force
# tc O(n^3), sc O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        output_set = set()

        for i in range(N-2):
            for j in range(i+1,N-1):
                for k in range(j+1, N):
                    if (nums[i]+nums[j]+nums[k] == 0):
                        output_set.add((nums[i], nums[j], nums[k]))
        output_list = [list(i) for i in output_set]
        return output_list

# two pointers
# tc O(n^2), sc O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        result = []
        nums.sort()
        N = len(nums)
        for i, value in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = N-1
            while l<r:
                sum_value = nums[i]+ nums[l]+ nums[r]
                if sum_value > 0:
                    r -= 1
                elif sum_value < 0:
                    l += 1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
        return result
