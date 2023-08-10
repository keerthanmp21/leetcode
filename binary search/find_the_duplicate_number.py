from typing import List


class Solution:
    # counting
    # tc O(n), sc O(n)
    def findDuplicate1(self, nums: List[int]) -> int:
        count = [0] * len(nums)

        for n in nums:
            count[n] += 1
            if count[n] > 1:
                return n

    # hash table
    # tc O(n), sc O(n)
    def findDuplicate2(self, nums: List[int]) -> int:
        visitSet = set()
        
        for n in nums:
            if n in visitSet:
                return n
            visitSet.add(n)

    # sorting
    # tc O(nlogn), sc O(logn)
    def findDuplicate3(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
        

    # two pointers
    # tc O(n), sc O(1)
    def findDuplicate4(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

    # binary search
    # tc O(nlogn), sc O(1)
    def findDuplicate5(self, nums: List[int]) -> int:
        '''
        We can use the binary search algorithm, each round we guess one number, then scan the input array, narrow the search range, and finally get the answer.

According to the Pigeonhole Principle, n+1n + 1n+1 integers, placed in an array of length nnn, at least 111 integer will be repeated.
        '''
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid
        return l
