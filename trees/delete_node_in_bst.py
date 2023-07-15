from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return 
        
        #if key found
        if root.val == key:
            #no left child
            if not root.left:
                return root.right
            
            #no right child
            if not root.right:
                return root.left

            #both child exist
            if root.left and root.right:
                #start with right
                temp = root.right
                
                #move left depth
                while temp.left:
                    temp = temp.left
                
                #replace value with min value
                root.val = temp.val

                #recurse on root.right with key == root.val
                root.right = self.deleteNode(root.right, root.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root