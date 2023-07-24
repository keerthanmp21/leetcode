from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # dfs
    # tc O(m*n) m = no. of nodes, n = no. of edges, sc O(m*n)
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copyNode = Node(node.val)
            oldToNew[node] = copyNode

            for neiNode in node.neighbors:
                copyNode.neighbors.append(dfs(neiNode))

            return copyNode

        return dfs(node) if node else None
    
    # bfs
    # tc O(m*n) m = no. of nodes, n = no. of edges, sc O(m*n)
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        q = deque([node])
        oldToNew = {node.val : Node(node.val,[])}

        while q:
            curr = q.popleft()
            curr_node = oldToNew[curr.val] 

            for neiNode in curr.neighbors:
                if neiNode.val not in oldToNew:
                    oldToNew[neiNode.val] = Node(neiNode.val,[])
                    q.append(neiNode)
                curr_node.neighbors.append(oldToNew[neiNode.val])

        return oldToNew[node.val]