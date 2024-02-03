package trees;

public class bt_zigzag_level_order_traversal {
    
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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if(root == null){
            return new ArrayList<>();
        }
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        boolean isRightToLeft = true;

        while(!q.isEmpty()){
            int size = q.size();
            List<Integer> temp = new ArrayList<>();

            for(int i = 0;i < size; i++){
                TreeNode node = q.poll();
                temp.add(node.val);
                if(node.left != null){
                     q.add(node.left);
                }
                if(node.right != null){
                    q.add(node.right);
                }
            }
            if(isRightToLeft){
                res.add(temp);
                isRightToLeft = false;
            }
            else{
                List<Integer> temp2 = new ArrayList<>();
                for (int i = temp.size() - 1; i >= 0; i--) {
                    temp2.add(temp.get(i));
                }
                res.add(temp2);
                isRightToLeft = true;
            }
        }

        return res;
    }
}