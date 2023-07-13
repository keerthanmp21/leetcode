from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # recursion
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        
    # dfs (stack)
    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        while stack:
            pNode, qNode = stack.pop()
            #reached end
            if not pNode and not qNode:
                continue
            #any one node is None
            elif not pNode or not qNode: 
                return False
            else:
                if pNode.val != qNode.val:
                    return False
                # if both node values are equal
                stack.append((pNode.left, qNode.left))
                stack.append((pNode.right, qNode.right))

        return True

    # queue(bfs)
    def isSameTree3(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q = [(p,q)]
        while q:
            pNode, qNode = q.pop(0)
            #reached end
            if not pNode and not qNode:
                continue
            #any one node is None
            elif not pNode or not qNode: 
                return False
            else:
                if pNode.val != qNode.val:
                    return False
                # if both node values are equal
                q.append((pNode.right, qNode.right))
                q.append((pNode.left, qNode.left))  

        return True






