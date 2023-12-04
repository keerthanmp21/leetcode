from typing import List
import collections
import heapq

class Solution:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
                
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
    
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:    
        if not nums or k == 1:
            return nums
        N = len(nums)
        maxHeap = []
        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i],i))
        res = [-maxHeap[0][0]]
        for i in range(k,N):
            while maxHeap[0][1] <= i-k:
                heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-nums[i],i))
            res.append(-maxHeap[0][0])
        return res
        