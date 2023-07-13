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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = 1+self.maxDepth(root.left)
        r = 1+self.maxDepth(root.right)
        return max(l,r)

    #bfs
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        q = deque([root])
        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
        