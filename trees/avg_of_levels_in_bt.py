from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # bfs
    def averageOfLevels1(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        res = []
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                temp.append(node.val)
            res.append(sum(temp) / len(temp))
        return res

    # dfs
    def averageOfLevels2(self, root: Optional[TreeNode]) -> List[float]:
        res = []

        def dfs(node, depth):
            if node:
                if len(res) <= depth:
                    res.append([0, 0])
                res[depth][0] += node.val
                res[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root, 0)
        return [sumVal / cnt for sumVal, cnt in res]
