//two pointers
//tc O(n), sc O(1)
public class trapping_rain_water {
    public int trap(int[] height) {
        if(height.length==0){
            return 0;
        }
        int l=0, r=height.length-1;
        int leftMax=height[l], rightMax=height[r];
        int res=0;
        while(l<r){
            if(leftMax<rightMax){
                leftMax=Math.max(leftMax,height[++l]);
                res += leftMax-height[l];
            }
            else{
                rightMax=Math.max(rightMax, height[--r]);
                res += rightMax-height[r];
            }
        }
        return res;
    }
}