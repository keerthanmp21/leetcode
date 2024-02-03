package trees;

public class max_depth_of_bt {
    
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
    // dfs
    public int maxDepth(TreeNode root) {
        if(root == null){
            return 0;
        }
        int l = 1 + maxDepth(root.left);
        int r = 1 + maxDepth(root.right);
        return Math.max(l, r);
    }
    
    // bfs
    public int maxDepth2(TreeNode root){
        if(root == null){
            return 0;
        }
        Deque<TreeNode> dq = new ArrayDeque<>();
        dq.offer(root);
        int res = 0;

        while(!dq.isEmpty()){
            res++;
            int size = dq.size();
            for(int i = 0; i < size; i++){
                TreeNode node = dq.poll();
                if(node.left != null){
                    dq.offer(node.left);
                }
                if(node.right != null){
                    dq.offer(node.right);
                }
            }
        }

        return res;
    }
}