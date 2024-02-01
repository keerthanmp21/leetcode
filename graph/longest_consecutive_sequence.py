from typing import List

class Solution:
    # brute force
    # time O(n * (n or len of longest)), space O(n)
    def longestConsecutive1(self, nums: List[int]) -> int:
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
    def longestConsecutive2(self, nums: List[int]) -> int:
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
            
            
            