from typing import Optional
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # dfs
    def amountOfTime1(self, root: Optional[TreeNode], start: int) -> int:
        neiNodes = defaultdict(list)

        def dfs(node):
            if not node:
                return
            if node.left:
                neiNodes[node.val].append(node.left.val)
                neiNodes[node.left.val].append(node.val)
                dfs(node.left) 
            if node.right:
                neiNodes[node.val].append(node.right.val)
                neiNodes[node.right.val].append(node.val)
                dfs(node.right)

        dfs(root)
        return self.getTime(neiNodes, start)

    # bfs
    def amountOfTime2(self, root: Optional[TreeNode], start: int) -> int:
        neiNodes = defaultdict(list)
        q = deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    neiNodes[node.val].append(node.left.val)
                    neiNodes[node.left.val].append(node.val)
                    q.append(node.left)
                if node.right:
                    neiNodes[node.val].append(node.right.val)
                    neiNodes[node.right.val].append(node.val)
                    q.append(node.right)

        return self.getTime(neiNodes, start)

    def getTime(self, neiNodes, start):
        q = deque([start])
        time = 0
        visited = set([start])
        while q:
            is_time_incr = False
            for _ in range(len(q)):
                nodeVal = q.popleft()
                for v in neiNodes[nodeVal]:
                    if v not in visited:
                        q.append(v)
                        visited.add(v)
                    else:
                        is_time_incr = True
            if is_time_incr:
                time += 1

        return time
        
                