from typing import List


class Solution:
    # brute force
    # tc O(n), sc O(2n)
    def sortArrayByParity1(self, nums: List[int]) -> List[int]:
        nums1 = []  # even
        nums2 = []  # odd

        for i in nums:
            if i % 2:
                nums2.append(i)
            else:
                nums1.append(i)
        # nums[:] = [i for i in nums if i%2==0] + [j for j in nums if j%2!=0]
        return nums1 + nums2

    # two pointers
    # tc O(n), sc O(1)
    def sortArrayByParity2(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            # l ind value is odd and r ind value is even
            if nums[l] % 2 == 1 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            # l ind value is odd and r ind value is odd
            elif nums[l] % 2 == 1:
                r -= 1
            # l ind value is even and r ind value is even
            else:
                l += 1

        return nums

    # two pointers
    # tc O(n), sc O(1)
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            # move l till we find odd
            while l < r and nums[l] % 2 == 0:
                l += 1
            # move r till we find even
            while l < r and nums[r] % 2 == 1:
                r -= 1

            nums[l], nums[r] = nums[r], nums[l]

        return nums
