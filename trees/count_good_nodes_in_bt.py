from collections import deque
from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # bfs
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()
        q.append((root,-inf))
        	

        while q:
            node,maxval = q.popleft()
            if node.val >= maxval:  
                res += 1
				
            if node.left:
                q.append((node.left,max(maxval,node.val)))
            
            if node.right:
                q.append((node.right,max(maxval,node.val)))
                
        return res

    # dfs
    def goodNodes2(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        return dfs(root, root.val)