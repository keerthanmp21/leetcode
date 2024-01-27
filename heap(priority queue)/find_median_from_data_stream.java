class MedianFinder {
    private PriorityQueue<Integer> small;
    private PriorityQueue<Integer> large;

    public MedianFinder() {
        small = new PriorityQueue<>(Collections.reverseOrder());
        large = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        if(!large.isEmpty() && num > large.peek()){
            large.add(num);
        }
        else{
            small.add(num);
        }
        if(small.size() > large.size() + 1){
            large.add(small.poll());
        }
        if(large.size() > small.size() + 1){
            small.add(large.poll());
        }
    }
    
    public double findMedian() {
        if(small.size() > large.size()){
            return small.peek();
        }
        else if (large.size() > small.size()){
            return large.peek();
        }
        else{
            return (double)(large.peek() + small.peek()) / 2;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */