from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        if root:
            queue.append(root)

        result = []
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(temp)
        return result

    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        # using deque
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
        return res
    
'''
Both `levelOrder` and `levelOrder2` functions perform level-order traversal (also known
 as breadth-first traversal) of a binary tree. Let's analyze their time and space 
 complexities.

### Time Complexity
For both implementations, the time complexity is \(O(N)\), where \(N\) is the number 
of nodes in the tree. This is because each node is visited exactly once during the 
traversal.

### Space Complexity
#### `levelOrder` (Using List as Queue)
- The space complexity is \(O(W)\), where \(W\) is the maximum width of the tree. In 
the worst case, especially for a complete binary tree, this can approach \(O(N)\) when 
all nodes at the last level are present.
- Additionally, since it uses a list and `pop(0)` is \(O(N)\), this can lead to 
inefficiencies. Inserting and deleting from the front of a list requires shifting 
elements.

#### `levelOrder2` (Using `deque`)
- The space complexity is also \(O(W)\) for the same reason as above, with the 
additional benefit of using a `deque` from the `collections` module. This allows for 
\(O(1)\) time complexity for appending and popping elements from both ends, making it 
more efficient than the list-based implementation.

### Summary
- **levelOrder (List-based):**
  - **Time Complexity:** \(O(N)\)
  - **Space Complexity:** \(O(W)\) (up to \(O(N)\) in the worst case)

- **levelOrder2 (Deque-based):**
  - **Time Complexity:** \(O(N)\)
  - **Space Complexity:** \(O(W)\) (up to \(O(N)\) in the worst case)

Overall, while both implementations have the same time complexity, `levelOrder2` 
is generally more efficient due to the use of `deque` for queue operations.
'''