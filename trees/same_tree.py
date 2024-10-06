from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # recursion
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        
    # dfs (stack)
    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        while stack:
            pNode, qNode = stack.pop()
            #reached end
            if not pNode and not qNode:
                continue
            #any one node is None
            elif not pNode or not qNode: 
                return False
            else:
                if pNode.val != qNode.val:
                    return False
                # if both node values are equal
                stack.append((pNode.left, qNode.left))
                stack.append((pNode.right, qNode.right))

        return True

    # queue(bfs)
    def isSameTree3(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q = [(p,q)]
        while q:
            pNode, qNode = q.pop(0)
            #reached end
            if not pNode and not qNode:
                continue
            #any one node is None
            elif not pNode or not qNode: 
                return False
            else:
                if pNode.val != qNode.val:
                    return False
                # if both node values are equal
                q.append((pNode.right, qNode.right))
                q.append((pNode.left, qNode.left))  

        return True




# recursion time and space complexity
'''
The function `isSameTree` compares two binary trees to determine if they are identical.
 Let's analyze its time and space complexity.

### Time Complexity
The time complexity of this algorithm is (O(N)), where (N) is the number of nodes in 
the trees. This is because in the worst case, we need to traverse all the nodes in 
both trees to check for equality. 

### Space Complexity
The space complexity is (O(H)), where (H) is the height of the trees. This space is 
used by the call stack during the recursive function calls. In the worst case 
(when the tree is skewed), the height can be (O(N)). In the best case (when the tree 
is balanced), the height is (O(log N)).

### Summary
- **Time Complexity:** (O(N))
- **Space Complexity:** (O(H)), where (H) is the height of the trees (up to (O(N))
 in the worst case).
'''


'''
Both `isSameTree2` (using DFS with a stack) and `isSameTree3` (using BFS with a queue)
 are effective implementations for checking if two binary trees are the same. 
 Let's analyze their time and space complexities.

### Time Complexity
For both `isSameTree2` and `isSameTree3`, the time complexity is \(O(N)\), where \(N\)
      is the number of nodes in the trees. This is because each node is visited exactly
        once during the traversal.

### Space Complexity
#### `isSameTree2` (DFS with Stack)
- The space complexity is \(O(H)\), where \(H\) is the height of the tree. In the worst 
case (skewed tree), this can be \(O(N)\), and in the best case (balanced tree), 
it will be \(O(\log N)\) due to the depth of the recursive calls stored in the stack.

#### `isSameTree3` (BFS with Queue)
- The space complexity for the BFS implementation is \(O(W)\), where \(W\) is the 
maximum width of the tree. In a complete binary tree, the maximum width can be 
approximately \(N/2\), leading to a space complexity of \(O(N)\) in the worst case. 
In a balanced tree, it is generally around \(O(\log N)\).

### Summary
- **isSameTree2 (DFS):**
  - **Time Complexity:** \(O(N)\)
  - **Space Complexity:** \(O(H)\) (up to \(O(N)\) in the worst case)

- **isSameTree3 (BFS):**
  - **Time Complexity:** \(O(N)\)
  - **Space Complexity:** \(O(W)\) (up to \(O(N)\) in the worst case)

Both approaches are efficient for solving the problem of checking if two binary trees 
are identical.
'''
