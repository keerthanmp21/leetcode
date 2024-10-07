from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # dfs1
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepth = self.DFS(root.left)
        rightDepth = self.DFS(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def DFS(self, root):
        if not root:
            return 0
        return 1 + self.DFS(root.left)

    # dfs2
    def countNodes2(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node):
            if node:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)

        return len(res)

    # bfs
    def countNodes3(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                res += 1
                q.append(node.left)
                q.append(node.right)

        return res