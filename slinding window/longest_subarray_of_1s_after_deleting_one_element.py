# tc O(n), sc O(1)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = res = 0
        k = 1 # max zero we can delete

        for r in range(len(nums)):
            # decrement k if we encounter 0
            if nums[r] == 0:
                k -= 1

            # if we have seen more than 1 zero then move l
            # till we discard first zero
            while k<0 and l<=r:
                if nums[l] == 0:
                    k += 1
                l += 1

            res = max(res,r-l)

        return res
