package stack;

import java.util.Stack;

public class asteroid_collision {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stk = new Stack<>();
        for(int i = 0; i < asteroids.length; i++){
            int a = asteroids[i];
            while(stk.size() != 0 && a<0 && stk.peek() > 0){
                int diff = stk.peek()+a;
                if(diff<0){
                    stk.pop();
                }
                else if(diff>0){
                    a = 0;
                }
                else{
                    a = 0;
                    stk.pop();
                }
            }
            if(a!=0){
                    stk.push(a);
            }
        }
        int[] res = new int[stk.size()];
        for(int i=0;i<stk.size();i++){
            res[i] = stk.get(i);
        }
        return res;
    }
}
