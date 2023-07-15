from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.checkLeaf(root1) == self.checkLeaf(root2)

    def checkLeaf(self, root):
        if not root:
            return []
        if not (root.left or root.right):
            return [root.val]
        return self.checkLeaf(root.left) + self.checkLeaf(root.right)