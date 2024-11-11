package dp;
public class longest_palindromic_substring{
    private boolean isPali(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    public String longestPalindrome1(String s) {
        int N = s.length();
        int startingIndex = 0;
        int maxLen = 0;

        // Check all substrings
        for (int i = 0; i < N; i++) {
            for (int j = i; j < N; j++) {
                if (isPali(s, i, j)) {
                    if ((j - i + 1) > maxLen) {
                        maxLen = j - i + 1;
                        startingIndex = i;
                    }
                }
            }
        }

        return s.substring(startingIndex, startingIndex + maxLen);
    }

    public String longestPalindrome2(String s) {
        String res = "";
        int resLen = 0;

        // Iterate through each character in the string
        for (int i = 0; i < s.length(); i++) {
            // Check for odd-length palindromes
            int l = i, r = i;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                if ((r - l + 1) > resLen) {
                    res = s.substring(l, r + 1);
                    resLen = r - l + 1;
                }
                l--;
                r++;
            }

            // Check for even-length palindromes
            l = i;
            r = i + 1;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                if ((r - l + 1) > resLen) {
                    res = s.substring(l, r + 1);
                    resLen = r - l + 1;
                }
                l--;
                r++;
            }
        }

        return res;
    }

    public String longestPalindrome3(String s) {
        int N = s.length();
        // Initialize the DP table
        boolean[][] dp = new boolean[N][N];

        // Every single character is a palindrome
        for (int i = 0; i < N; i++) {
            dp[i][i] = true;
        }

        String res = s.substring(0, 1); // The first character is the initial result

        // Fill the DP table
        for (int i = N - 1; i >= 0; i--) {
            for (int j = i + 1; j < N; j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    if (j - i == 1 || dp[i + 1][j - 1]) {
                        dp[i][j] = true;
                        if (j - i + 1 > res.length()) {
                            res = s.substring(i, j + 1);
                        }
                    }
                }
            }
        }

        return res;
    }
}