from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.checkPath(root, 0, targetSum)

    def checkPath(self, root, curSum, targetSum):
        if not root:
            return False
        if not root.left and not root.right:  # leaf node
            return curSum + root.val == targetSum

        return self.checkPath(
            root.left, curSum + root.val, targetSum
        ) or self.checkPath(root.right, curSum + root.val, targetSum)
