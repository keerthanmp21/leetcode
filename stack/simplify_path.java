package stack;

import java.util.Stack;

public class simplify_path {
    public String simplifyPath(String path) {
        Stack<String> stk = new Stack<>();
        String sr[] = path.split("/");
        for(String s: sr){
            if(stk.size() != 0 && s.equals("..")){
                stk.pop();
            }
            else if(!(s.equals("") || s.equals(".") || s.equals(".."))){
                stk.push(s);
            }
        }
        return "/"+String.join("/",stk);
    }
}
