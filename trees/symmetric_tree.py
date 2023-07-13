from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.checkSym(root.left, root.right)
        
    def checkSym(self,l,r):
        # we can all 3 approaches of same tree here
        if not l and not r:
            return True
        elif not l or not r:
            return False
        elif l.val != r.val:
            return False
        
        return self.checkSym(l.left,r.right) and self.checkSym(l.right,r.left)