import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.minHeap = []
        self.next_num = 1

    def popSmallest(self) -> int:
        if self.minHeap:
            return heapq.heappop(self.minHeap)
        res = self.next_num
        self.next_num += 1
        return res

    def addBack(self, num: int) -> None:
        if num < self.next_num and num not in self.minHeap:
            heapq.heappush(self.minHeap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)