package trees;

public class same_tree {
    
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
    // dfs using recursion
    public boolean isSameTree1(TreeNode p, TreeNode q) {
        if(p == null && q == null){
            return true;
        }
        if(p == null || q == null || p.val != q.val){
            return false;
        }
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }

    // dfs using stack
    public boolean isSameTree2(TreeNode p, TreeNode q){
        Stack<TreeNode[]> stack = new Stack<>();
        stack.add(new TreeNode[]{p, q});

        while(!stack.isEmpty()){
            TreeNode[] nodes = stack.pop();
            TreeNode pNode = nodes[0];
            TreeNode qNode = nodes[1];
            //reached end
            if(pNode == null && qNode == null){
                continue;
            }
            // any one node is None
            else if(pNode == null || qNode == null){
                return false;
            }
            else{
                if(pNode.val != qNode.val){
                    return false;
                }
                // if both node values are equal
                stack.add(new TreeNode[]{pNode.left, qNode.left});
                stack.add(new TreeNode[]{pNode.right, qNode.right});
            }
        }

        return true;
    }

    // bfs
    public boolean isSameTree3(TreeNode p, TreeNode q){
        Deque<TreeNode[]> queue = new ArrayDeque<>();
        queue.offer(new TreeNode[]{p, q});

        while(!queue.isEmpty()){
            TreeNode[] nodes = queue.pop();
            TreeNode pNode = nodes[0];
            TreeNode qNode = nodes[1];
            //reached end
            if(pNode == null && qNode == null){
                continue;
            }
            // any one node is None
            else if(pNode == null || qNode == null){
                return false;
            }
            else{
                if(pNode.val != qNode.val){
                    return false;
                }
                // if both node values are equal
                queue.offer(new TreeNode[]{pNode.left, qNode.left});
                queue.offer(new TreeNode[]{pNode.right, qNode.right});
            }
        }
        return true;
    }
}