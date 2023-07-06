package stack;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class valid_parenthese {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();
        Map<Character, Character> closeToOpen = new HashMap<>();
        closeToOpen.put(')','(');
        closeToOpen.put('}','{');
        closeToOpen.put(']','[');
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(closeToOpen.containsKey(c)){
                if(stk.size() != 0 && stk.peek() == closeToOpen.get(c)){
                    stk.pop();
                }
                else{
                    return false;
                }
            }
            else{
                stk.push(c);
            }     
        }
        if(stk.size() == 0){
            return true;
        }
        else{
            return false;
        }
    }
}
