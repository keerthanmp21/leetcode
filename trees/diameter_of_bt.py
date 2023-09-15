from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree1(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res[0] = max(res[0], left + right)
            return 1 + max(left, right)

        dfs(root)
        return res[0]

    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res = max(self.res, left + right)
        return 1 + max(left, right)
