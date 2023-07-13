from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], left=float('-infinity'), right=float('infinity')) -> bool:
        if not root:
            return True
        if root.val <= left or root.val >= right:
            return False
        return self.isValidBST(root.left, left, root.val) and self.isValidBST(root.right, root.val, right)

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and root.val <= prev.val:
                return False
            prev = root
            root = root.right
        return True
        