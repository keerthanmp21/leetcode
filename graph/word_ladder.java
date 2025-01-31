import java.util.*;

public class word_ladder {
    
}

class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if(!wordList.contains(endWord)){
            return 0;
        }
        
        Map<String, List<String>> adjList = new HashMap<>();
        wordList.add(beginWord);
        for(String word : wordList){
            for(int i = 0; i < word.length(); i++){
                String pattern = word.substring(0, i) + '*' + word.substring(i + 1);
                List<String> words = adjList.getOrDefault(pattern, new ArrayList<>());
                words.add(word);
                adjList.put(pattern, words);
            }
        }

        Queue<String> q = new LinkedList<>();
        q.add(beginWord);
        int res = 1;
        Set<String> visited = new HashSet<>();

        while(!q.isEmpty()){
            int size = q.size();
            for(int k = 0; k < size; k++){
                String curWord = q.poll();
                if(curWord.equals(endWord)){
                    return res;
                }
                for(int i = 0; i < curWord.length(); i++){
                    String pattern = curWord.substring(0, i) + '*' + curWord.substring(i + 1);
                    for(String neiWord : adjList.getOrDefault(pattern, new ArrayList<>())){
                        if(!visited.contains(neiWord)){
                            visited.add(neiWord);
                            q.add(neiWord);
                        }
                    }
                }
            }
            res++;
        }

        return 0;

    }
}