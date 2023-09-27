from typing import List


class Solution:
    # brute force
    def nextGreaterElement1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]), len(nums2)):
                if nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
        return res

    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        stack = []
        hm = {}
        stack.append(nums2[-1])

        for i in range(len(nums2) - 2, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                hm[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            if nums1[i] in hm:
                res[i] = hm[nums1[i]]
        return res
