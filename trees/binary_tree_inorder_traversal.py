from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # recursion
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        

    # stack, inorder (lvr)
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        while root or stack:
            while root:
                # left
                stack.append(root)
                root = root.left
            root = stack.pop()
            # visit
            res.append(root.val)
            # right
            root = root.right
        return res