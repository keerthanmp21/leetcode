package dp;


import java.util.HashMap;
import java.util.Map;

public class maximum_product_subarray {
    
    // Brute Force - O(n^2) time complexity, O(1) space complexity
    public int maxProduct1(int[] nums) {
        int N = nums.length;
        int res = Integer.MIN_VALUE;
        for (int i = 0; i < N; i++) {
            int cur = 1;
            for (int j = i; j < N; j++) {
                cur *= nums[j];
                res = Math.max(res, cur);
            }
        }
        return res;
    }

    // Backtracking - O(2^n) time complexity, O(1) space complexity
    public int maxProduct2(int[] nums) {
        int N = nums.length;
        
        // Helper method for backtracking
        return backtrack(nums, 0, 1, N);
    }

    private int backtrack(int[] nums, int idx, int value, int N) {
        if (idx == N) {
            return value;
        }
        
        // Choose to include current number or skip it
        int pick = backtrack(nums, idx + 1, value * nums[idx], N);
        int notPick = backtrack(nums, idx + 1, nums[idx], N);
        
        if (idx == 0) {
            value = nums[0];
        }
        
        return Math.max(value, Math.max(pick, notPick));
    }

    // DP with Memoization - O(n^2) time complexity, O(n) space complexity
    public int maxProduct3(int[] nums) {
        int N = nums.length;
        Map<String, Integer> dp = new HashMap<>();
        
        // Helper method for backtracking with memoization
        return backtrack(nums, 0, 1, N, dp);
    }

    private int backtrack2(int[] nums, int idx, int value, int N, Map<String, Integer> dp) {
        if (idx == N) {
            return value;
        }

        // Memoization key
        String key = idx + "," + value;
        if (dp.containsKey(key)) {
            return dp.get(key);
        }

        // Choose to include current number or skip it
        int pick = backtrack(nums, idx + 1, value * nums[idx], N, dp);
        int notPick = backtrack(nums, idx + 1, nums[idx], N, dp);

        if (idx == 0) {
            value = nums[0];
        }

        int res = Math.max(value, Math.max(pick, notPick));
        dp.put(key, res);
        
        return res;
    }

    // DP with Memoization using @Cache - Java doesn't have built-in cache annotation, so similar memoization is implemented manually.
    public int maxProduct4(int[] nums) {
        int N = nums.length;
        
        // Using a cache map to avoid recalculating results
        Map<String, Integer> cache = new HashMap<>();
        return backtrack(nums, 0, 1, N, cache);
    }

    private int backtrack(int[] nums, int idx, int value, int N, Map<String, Integer> cache) {
        if (idx == N) {
            return value;
        }

        String key = idx + "," + value;
        if (cache.containsKey(key)) {
            return cache.get(key);
        }

        // Choose to include current number or skip it
        int pick = backtrack(nums, idx + 1, value * nums[idx], N, cache);
        int notPick = backtrack(nums, idx + 1, nums[idx], N, cache);

        if (idx == 0) {
            value = nums[0];
        }

        int res = Math.max(value, Math.max(pick, notPick));
        cache.put(key, res);
        
        return res;
    }

    // DP Tabulation - O(n) time complexity, O(1) space complexity
    public int maxProduct5(int[] nums) {
        int res = Integer.MIN_VALUE;
        int curMin = 1, curMax = 1;

        for (int n : nums) {
            if (n == 0) {
                curMin = curMax = 1;
                continue;
            }
            
            int tmp = curMax * n;
            curMax = Math.max(n * curMax, Math.max(n * curMin, n));
            curMin = Math.min(tmp, Math.min(n * curMin, n));
            
            res = Math.max(res, curMax);
        }
        
        return res;
    }
}
