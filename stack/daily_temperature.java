package stack;

import java.util.Stack;

public class daily_temperature {
    / brute force (tle)
    // time O(n^2), space O(n)
    public int[] dailyTemperatures1(int[] temperatures) {
        int N = temperatures.length;
        int[] res = new int[N];

        for(int i = 0; i < N; i++){
            int t1 = temperatures[i];
            for(int j = i + 1; j < N; j++){
                int t2 = temperatures[j];
                if(t2 > t1){
                    res[i] = (j - i);
                    break;
                }
            }
        }

        return res;
    }

        // monotonic decreasing stack
    // time O(n), space O(n)
    public int[] dailyTemperatures(int[] temperatures){
        int N = temperatures.length;
        int[] res = new int[N];
        Stack<Integer> stk = new Stack<>();

        for(int i = 0; i < N; i++){
            int curT = temperatures[i];
            while(!stk.isEmpty() && curT > temperatures[stk.peek()]){
                int topInd = stk.pop();
                res[topInd] = i - topInd;
            }
            stk.push(i);
        }

        return res;
    }
}
