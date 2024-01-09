from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # dfs
    def rangeSumBST1(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []

        def dfs(node):
            if not node:
                return
            if node.val >= low and node.val <= high:
                res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return sum(res)

    # bfs
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []
        q = deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.val >= low and node.val <= high:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return sum(res)