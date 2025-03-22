from typing import List

class UnionFind:
    def __init__(self, nums):
        self.parent = {num: num for num in nums}
        self.rank = {num:1 for num in nums}

    def find(self, num):
        # if self.parent[num] != num:
        #     self.parent[num] = self.find(self.parent[num])  # Path compression
        # return self.parent[num]

        while num != self.parent[num]:  
            self.parent[num] = self.parent[self.parent[num]]  # Path compression (flatten tree)
            num = self.parent[num]  # Move up the tree
        return num

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:  # If they are not already connected
            if self.rank[rootA] > self.rank[rootB]:
                self.parent[rootB] = rootA
                self.rank[rootA] += self.rank[rootB]  # Increase size of rootX
            else:
                self.parent[rootA] = rootB
                self.rank[rootB] += self.rank[rootA]  # Increase size of rootY


class Solution:
    # brute force
    # time O(n * (n or len of longest)), space O(n)
    def longestConsecutive1(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            length = 0
            while (num + length) in nums:
                length += 1
            longest = max(longest, length)

        return longest

    # brute force
    # time O(n * (n or len of longest)), space O(n)
    def longestConsecutive2(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest

    # union find
    # time O(n), space O(n)
    def longestConsecutive3(self, nums: List[int]) -> int:
        if not nums:
            return 0
        node = {} #value = parent node
        rank = {}


        for i in nums:
            node[i] = i
            rank[i] = 0
        for key, value in node.items():
            parent = value + 1
            if parent in node:
                node[key] = node[parent]
                
        for par in node.keys():
            p = node[par]
            while p != node[p]:
                node[p] = node[node[p]]
                p =node[p]
            #print(p, node[p])
            rank[p] += 1
            
        #print(rank)
        return max(rank.values())
            

    # time complexity O(N)
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        uf = UnionFind(nums)

        for num in nums:
            if (num + 1) in uf.parent:
                uf.union(num, num + 1)
            
        return max(uf.rank.values(), default = 0)