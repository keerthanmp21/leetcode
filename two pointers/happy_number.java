public class happy_number {
    
}
class Solution {
    public boolean isHappy(int n) {
        int fast=n, slow=n;
        while(true){
            slow = sumOfSquare(slow);
            fast = sumOfSquare(sumOfSquare(fast));
            if(slow==fast){
                break;
            }
        }
        if(slow==1){
            return true;
        }
        else{
            return false;
        }
    }
    public int sumOfSquare(int n){
        int output = 0;
        while(n>0){
            int digit = n%10;
            digit = (int)Math.pow(digit,2);
            output = output+digit;
            n = (int)Math.floor(n/10);
        }
        return output;
    }
}