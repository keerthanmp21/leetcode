class Solution {
    public int maxArea(int[] height) {
        int l = 0;
        int r = height.length-1;
        int maxArea = 0;
        int res = 0;
        while(l<r){
            maxArea = (r-l)*Math.min(height[l], height[r]);
            res = Math.max(res, maxArea);
            if(height[l]<height[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return res;
    }
}