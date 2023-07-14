from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    # bfs
    # tc O(n), sc O(n)
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque([root])
        while q:
            rightNode = None
            for _ in range(len(q)):
                node = q.popleft()
                node.next = rightNode
                rightNode = node
                if node.right:
                    q.append(node.right)
                    q.append(node.left)
        return root

    #dfs
    # tc O(n), sc O(logn)
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        leftNode, rightNode, nextNode = root.left, root.right, root.next
        if leftNode:
            leftNode.next = rightNode
            if nextNode:
                rightNode.next = nextNode.left
            self.connect(leftNode)
            self.connect(rightNode)
        return root


