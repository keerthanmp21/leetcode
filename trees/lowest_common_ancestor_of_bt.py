# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root

        leftSubTree = self.lowestCommonAncestor(root.left, p, q)
        rightSubTree = self.lowestCommonAncestor(root.right, p, q)

        if leftSubTree and rightSubTree:
            return root

        # if p or q is not found at right then process with left subtree
        if leftSubTree:
            return leftSubTree

        # if p or q is not found at right then process with right subtree
        if rightSubTree:
            return rightSubTree

        return None
