class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        HashMap<Integer, Integer> noOfOccurrences = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++){
            int value = noOfOccurrences.getOrDefault(nums[i], 0) + 1;
            noOfOccurrences.put(nums[i], value);
        }
        System.out.println(noOfOccurrences);

        List<List<Integer>> res = new ArrayList<>();
        int maxOccurrences = noOfOccurrences.values().stream().max(Integer::compare).orElse(0);

        for (int i = 0; i < maxOccurrences; i++) {
            List<Integer> temp = new ArrayList<>();
            for (Map.Entry<Integer, Integer> entry : new ArrayList<>(noOfOccurrences.entrySet())) {
                int key = entry.getKey();
                int value = entry.getValue();
                if (value != 0) {
                    temp.add(key);
                }
                noOfOccurrences.put(key, value - 1);
                if (noOfOccurrences.get(key) == 0) {
                    noOfOccurrences.remove(key);
                }
            }
            res.add(temp);
        }

        return res;
    }
}