public class container_with_most_waters {
    // brute force
    // tc O(n^2), sc O(n)
    public int maxArea1(int[] height) {
        int N = height.length;
        int res = 0;
        for(int i = 0; i < N - 1; i++){
            for(int j = i + 1; j < N; j++){
                int area = (j - i) * Math.min(height[i], height[j]);
                res = Math.max(res, area);
            }
        }
        return res;
    }

    // two pointers
    // tc O(n), sc O(n)
    public int maxArea(int[] height) {
        int l = 0, r = height.length - 1;
        int res = 0;
        while(l < r){
            int area = (r - l) * Math.min(height[l], height[r]);
            res = Math.max(res, area);
            if(height[l] < height[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return res;
    }
}