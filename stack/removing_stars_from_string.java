package stack;

import java.util.Stack;

public class removing_stars_from_string {
    public String removeStars(String s) {
        Stack<String> stk = new Stack<>();
        for(int i=0; i<s.length(); i++){
            String c = ""+s.charAt(i);
            if(c.equals("*")){
                stk.pop();
            }
            else{
                stk.push(c);
            }
        }
        return String.join("",stk);
    }
}
