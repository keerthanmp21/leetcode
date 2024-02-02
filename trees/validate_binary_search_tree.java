package trees;

public class validate_binary_search_tree {
    
}

//Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public boolean isValidBST1(TreeNode root) {
        return checkValidBST(root, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY);
    }

    private boolean checkValidBST(TreeNode root, double left, double right){
        if(root == null){
            return true;
        }
        if(root.val <= left || root.val >= right){
            return false;
        }
        return checkValidBST(root.left, left, root.val) && checkValidBST(root.right, root.val, right);
    }

    public boolean isValidBST2(TreeNode root){
        Stack<TreeNode> stack = new Stack<>();
        TreeNode prev = null;
        
        while(root != null || !stack.isEmpty()){
            while(root != null){
                stack.add(root);
                root = root.left;
            }
            root = stack.pop();
            if(prev != null && root.val <= prev.val){
                return false;
            }
            prev = root;
            root = root.right;
        }

        return true;
    }
}