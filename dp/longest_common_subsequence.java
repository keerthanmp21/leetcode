package dp;

import java.util.Arrays;

public class longest_common_subsequence {
    
}

class Solution {
    public int longestCommonSubsequence1(String text1, String text2){
        return backtrack(0, 0, text1, text2);
    }

    private int backtrack(int i, int j, String text1, String text2){
        if(i == text1.length() || j == text2.length()){
            return 0;
        }
        if(text1.charAt(i) == text2.charAt(j)){
            return 1 + backtrack(i + 1, j + 1, text1, text2);
        }
        else{
            return Math.max(backtrack(i + 1, j, text1, text2),
            backtrack(i, j + 1, text1, text2));
        }
    }

    public int longestCommonSubsequence(String text1, String text2){
        int[][] memo = new int[text1.length()][text2.length()];
        for (int[] row : memo) {
            Arrays.fill(row, -1); // Initialize with -1 (uncomputed)
        }
        return backtrack(0, 0, text1, text2, memo);
    }

    private int backtrack(int i, int j, String text1, String text2, int[][] memo){
        if(i == text1.length() || j == text2.length()){
            return 0;
        }
        if(memo[i][j] != -1){
            return memo[i][j];
        }
        if(text1.charAt(i) == text2.charAt(j)){
            memo[i][j] = 1 + backtrack(i + 1, j + 1, text1, text2, memo);
        }
        else{
            memo[i][j] = Math.max(backtrack(i + 1, j, text1, text2, memo),
            backtrack(i, j + 1, text1, text2, memo));
        }
        return memo[i][j];
    }

    public int longestCommonSubsequence3(String text1, String text2) {
        int M = text1.length();
        int N = text2.length();

        int[][] dp = new int[M + 1][N + 1];

        for(int i = M - 1; i > -1; i--){
            for(int j = N - 1; j > -1; j--){
                if(text1.charAt(i) == text2.charAt(j)){
                    dp[i][j] = 1 + dp[i + 1][j + 1];
                }
                else{
                    dp[i][j] = Math.max(dp[i][j + 1], dp[i + 1][j]);
                }
            }
        }

        return dp[0][0];
    }
}