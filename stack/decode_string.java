package stack;

import java.util.Stack;

public class decode_string {
    public String decodeString(String s) {
        Stack<String> stk = new Stack<>();
        String curString = "";
        int curDigit = 0;
        for(int i=0; i<s.length(); i++){
            char chr = s.charAt(i);
            if(chr == '['){
                stk.push(curString);
                curString = "";
                stk.push(""+curDigit);
                curDigit = 0;
            }
            else if(chr == ']'){
                int prevDigit = Integer.parseInt(stk.pop());
                String prevString = stk.pop();
                curString = prevString + curString.repeat(prevDigit);
            }
            else if(Character.isDigit(chr)){
                curDigit = curDigit*10 + (chr-48);
            }
            else{
                curString = curString + chr;

            }
        }
        return curString;
    }
}
