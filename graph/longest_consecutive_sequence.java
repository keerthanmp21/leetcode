class Solution {
    // brute force
    // time O(n * (n or len of longest)), space O(n)
    public int longestConsecutive1(int[] nums) {
        int longest = 0;
        Set<Integer> numSet = new HashSet<>();
        for(int n : nums){
            numSet.add(n);
        }

        for(int n : nums){
            if(!numSet.contains(n - 1)){
                int len = 0;
                while(numSet.contains(n + len)){
                    len++;
                }
                longest = Math.max(longest, len);
            }
        }

        return longest;
    }

    // union find
    // time O(n), space O(n)
    public int longestConsecutive2(int[] nums){
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        HashMap<Integer, Integer> node = new HashMap<>(); // value = parent node
        HashMap<Integer, Integer> rank = new HashMap<>();

        for (int i : nums) {
            node.put(i, i);
            rank.put(i, 0);
        }

        for (int key : node.keySet()) {
            int parent = node.get(key) + 1;
            if (node.containsKey(parent)) {
                node.put(key, node.get(parent));
            }
        }

        for (int par : node.keySet()) {
            int p = node.get(par);
            while (p != node.get(p)) {
                node.put(p, node.get(node.get(p)));
                p = node.get(p);
            }
            rank.put(p, rank.getOrDefault(p, 0) + 1);
        }

        int maxRank = 0;
        for (int value : rank.values()) {
            maxRank = Math.max(maxRank, value);
        }

        return maxRank;

    }
}