class Solution {
    public boolean find132pattern(int[] nums) {
        Stack<Integer> stack = new Stack<>();
        int k_val = Integer.MIN_VALUE;

        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] < k_val) {
                return true;
            }
            // Monotonic decreasing
            while (!stack.isEmpty() && nums[i] > stack.peek()) {
                k_val = stack.pop();
            }
            stack.push(nums[i]);
        }

        return false;
    }
}