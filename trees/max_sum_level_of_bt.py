from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # bfs
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum, level, maxLevel = float("-inf"), 0, 0
        q = deque([root])
        while q:
            level += 1
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level_sum > maxSum:
                maxSum, maxLevel = level_sum, level
        return maxLevel

    # dfs
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        l = []

        def dfs(node, level):
            if not node:
                return
            if len(l) == level:
                l.append(node.val)
            else:
                l[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return 1 + l.index(max(l))
