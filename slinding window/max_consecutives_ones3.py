# tc O(n), sc O(1)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = res = cur_count = 0
        while r<len(nums):
            if nums[r] == 1:
                r += 1
                cur_count += 1
            elif nums[r] == 0 and k>0:
                k -= 1
                r += 1
                cur_count += 1
            else:
                res = max(res, cur_count)
                while nums[l] == 1:
                    l += 1
                cur_count = r-l
                l += 1
                r += 1
        return max(res,cur_count)
