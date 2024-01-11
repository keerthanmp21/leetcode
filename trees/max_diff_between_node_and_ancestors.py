from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # brute-force
    # time O(n * n), space O(n)
    def maxAncestorDiff1(self, root: Optional[TreeNode]) -> int:
        maxVal = [float('-inf')]
        def dfs(node, childNode):
            if not node:
                return
            if not childNode:
                return
            maxVal[0] = max(maxVal[0], abs(node.val - childNode.val))
            dfs(node, childNode.left)
            dfs(node, childNode.right)
            dfs(childNode, childNode.left)
            dfs(childNode, childNode.right)

        dfs(root, root.left)
        dfs(root, root.right)

        return maxVal[0]

    # dfs
    # time O(n), space O(n)
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(node, minVal, maxVal):
            if not node:
                return maxVal - minVal
            tempMin = min(minVal, node.val)
            tempMax = max(maxVal, node.val)

            return max(dfs(node.left, tempMin, tempMax),
            dfs(node.right, tempMin, tempMax))


        return dfs(root, root.val, root.val)