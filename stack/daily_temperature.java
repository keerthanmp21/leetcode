package stack;

import java.util.Stack;

public class daily_temperature {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stk = new Stack<>();
        int []res = new int[temperatures.length];

        for(int i=0; i<temperatures.length; i++){
            while(!stk.isEmpty() && temperatures[i]>temperatures[stk.peek()]){
                int topInd = stk.pop();
                res[topInd] = i-topInd;
            }
            stk.push(i);
        }

        return res;
    }
}
