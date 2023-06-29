# brute force
# tc O(nlogn), sc O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()

# two pointers
# tc O(n), sc O(1)
class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l, r, i = m-1, m+n-1, n-1
        while i>=0:
            if l>=0 and nums1[l]>nums2[i]:
                nums1[r] = nums1[l]
                l -= 1
            else:
                nums1[r] = nums2[i]
                i -= 1
            r -= 1
        