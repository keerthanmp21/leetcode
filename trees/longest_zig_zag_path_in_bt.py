from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0

        def dfs(node, deep, dir):
            self.maxLength = max(self.maxLength, deep)

            if node.left is not None:
                dfs(node.left, deep + 1, "left") if dir != "left" else dfs(
                    node.left, 1, "left"
                )
            if node.right is not None:
                dfs(node.right, deep + 1, "right") if dir != "right" else dfs(
                    node.right, 1, "right"
                )

        dfs(root, 0, "")
        return self.maxLength
