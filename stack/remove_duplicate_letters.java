class Solution {
    public String removeDuplicateLetters(String s) {
        HashMap<Character, Integer> last_index = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            last_index.put(s.charAt(i), i);
        }

        Stack<Character> stack = new Stack<>();
        HashSet<Character> visited = new HashSet<>();

        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            if (!visited.contains(currentChar)) {
                while (!stack.isEmpty() && stack.peek() > currentChar && last_index.get(stack.peek()) > i) {
                    visited.remove(stack.pop());
                }
                stack.push(currentChar);
                visited.add(currentChar);
            }
        }

        StringBuilder result = new StringBuilder();
        for (char c : stack) {
            result.append(c);
        }
        return result.toString();

    }
}