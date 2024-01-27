class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<List<Integer>> output = new ArrayList<>();
        List<int[]> points = new ArrayList<>();

        for (int[] building : buildings) {
            int start = building[0];
            int end = building[1];
            int height = building[2];

            points.add(new int[]{start, -height});
            points.add(new int[]{end, height});
        }

        points.sort((a, b) -> {
            if (a[0] != b[0]) {
                return a[0] - b[0];
            } else {
                return a[1] - b[1];
            }
        });

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        maxHeap.offer(0);
        int prevMaxHeight = 0;

        for (int[] point : points) {
            int x = point[0];
            int h = Math.abs(point[1]);

            if (point[1] < 0) {
                maxHeap.offer(h);
            } else {
                maxHeap.remove(h);
            }

            int currMaxHeight = maxHeap.peek();
            if (prevMaxHeight != currMaxHeight) {
                List<Integer> newPoint = new ArrayList<>();
                newPoint.add(x);
                newPoint.add(currMaxHeight);
                output.add(newPoint);
                prevMaxHeight = currMaxHeight;
            }
        }

        return output;
    }
}