# bucket sort
# tc O(n), sc O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        for num, cnt in count.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# heap(priority queue)
# tc O(klogn), sc O(n)
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        no_of_occurences = Counter(nums)
        maxHeap = [(-value, key) for key, value in no_of_occurences.items()]
        heapq.heapify(maxHeap)
        res = []
        for i in range(k):
            _, value = heapq.heappop(maxHeap)
            res.append(value)
        return res