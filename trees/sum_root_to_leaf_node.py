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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root, pathSum):
            if root:
                # leaf node
                if not root.left and not root.right:
                    pathSum = pathSum * 10 + root.val
                    res[0] += pathSum
                dfs(root.left, pathSum * 10 + root.val)
                dfs(root.right, pathSum * 10 + root.val)

        dfs(root, 0)
        return res[0]

    # bfs
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = 0

        while q:
            node = q.popleft()
            if not node.left and not node.right:
                res += node.val
            if node.left:
                node.left.val += node.val * 10
                q.append(node.left)
            if node.right:
                node.right.val += node.val * 10
                q.append(node.right)

        return res
