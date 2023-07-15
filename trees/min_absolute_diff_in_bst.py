from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node, l, h):
            if not node:
                return h-l
            left = dfs(node.left, l, node.val)
            right = dfs(node.right, node.val, h)
            return min(left, right)
        return dfs(root, float("-infinity"), float("infinity"))