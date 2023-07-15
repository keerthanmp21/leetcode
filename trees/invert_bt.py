from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # dfs(recursive)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        l = self.invertTree(root.right)
        r = self.invertTree(root.left)
        root.left = l
        root.right = r

        return root
        

    # dfs(stack)
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.right, node.left = node.left, node.right
                stack.extend([node.right, node.left])

        return root
        
    # bfs
    def invertTree3(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                node.right, node.left = node.left, node.right
                q.append(node.left)
                q.append(node.right)         

        return root