import java.util.*;
// tc O(n), sc O(n)
public class find_all_anagrams_in_string {
    public List<Integer> findAnagrams(String s, String p) {
        int sLen = s.length(), pLen = p.length();
        if(pLen>sLen){
            return Collections.emptyList();
        }
        HashMap<Character,Integer> sCount = new HashMap<Character,Integer>();
        HashMap<Character,Integer> pCount = new HashMap<Character,Integer>();

        for(int i=0; i<pLen;i++){
            char s_char = s.charAt(i);
            if(sCount.containsKey(s_char)){
                sCount.put(s_char,sCount.get(s_char)+1);
            }
            else{
                sCount.put(s_char,1);
            }
            char p_char = p.charAt(i);
            if(pCount.containsKey(p_char)){
                pCount.put(p_char,pCount.get(p_char)+1);
            }
            else{
                pCount.put(p_char,1);
            }
        }

        ArrayList<Integer> res = new ArrayList<Integer>();
        if(sCount.equals(pCount)){
            res.add(0);
        }
        
        int l = 0;
        for(int r = pLen; r<sLen; r++){
            char r_char = s.charAt(r);
            if(sCount.containsKey(r_char)){
                sCount.put(r_char, sCount.get(r_char)+1);
            }
            else{
                sCount.put(r_char,1);
            }
            sCount.put(s.charAt(l), sCount.get(s.charAt(l))-1);
            if(sCount.get(s.charAt(l)) == 0){
                sCount.remove(s.charAt(l));
            }
            l++;
            if(sCount.equals(pCount)){
                res.add(l);
            }
        }
        return res;







    }

}